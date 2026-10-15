"""Fail-closed YAML subset and contract boundaries. No semantic authorization claims."""
import yaml
from yaml import events, nodes

LIMIT = 1024 * 1024


DOMAINS = ('professional_delivery', 'research_learning', 'personal_life', 'systems_automation', 'experimentation', 'creative_media')
OWNERS = tuple(d + '_owner' for d in DOMAINS)
OWNER = OWNERS[0]


class BoundaryError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise BoundaryError(message)


def shape(value, fields, optional=()):
    require(type(value) is dict, 'Expected mapping')
    require(set(fields) <= value.keys() and value.keys() <= set(fields) | set(optional), 'Missing/extra fields: ' + ','.join(fields))


def text(value, empty=False):
    require(type(value) is str and (empty or bool(value.strip())), 'Expected nonempty string')


def strings(value, unique=False):
    require(type(value) is list, 'Expected string list')
    for item in value:
        text(item)
    require(not unique or len(value) == len(set(value)), 'Duplicate list identifier')


def initiative(value, allow_empty=False):
    shape(value, ('objective',), ('context',))
    text(value['objective'], empty=allow_empty)
    if 'context' in value:
        text(value['context'], empty=True)


def governor(value):
    shape(value, ('decision', 'reason', 'next_owner'))
    require(value['decision'] in ('proceed', 'stop', 'clarify'), 'Governor decision')
    text(value['reason'])
    require(value['next_owner'] == ('orchestrator' if value['decision'] == 'proceed' else None), 'Governor route')


def orchestrator(value, objective, candidates=OWNERS):
    shape(value, ('orchestration_status', 'reason', 'initiative_state', 'next_action'))
    status = value['orchestration_status']
    require(status in ('clarify', 'planning', 'ready'), 'Orchestrator status')
    text(value['reason'])
    n = value['next_action']
    shape(n, ('type', 'target'))
    routes = {'clarify': ('request_governance_clarification', 'governor'), 'planning': ('convene_planning_room', 'planning_room'), 'ready': ('handoff', 'domain_owner')}
    require((n['type'], n['target']) == routes[status], 'Orchestrator route')
    s = value['initiative_state']
    shape(s, ('objective', 'scope', 'team', 'decisions', 'assumptions', 'blockers', 'work', 'success_criteria', 'what_happens_first', 'requested_contributions'))
    text(s['objective'], empty=status == 'clarify')
    require(s['objective'] == objective, 'Original objective changed')
    if not s['objective'].strip():
        require(s['team'] == {'lead_owner': None, 'participating_owners': []} and
                all(s[field] == [] for field in ('work', 'decisions', 'assumptions', 'success_criteria', 'requested_contributions')),
                'Empty objective clarification must not authorize work')
    shape(s['scope'], ('in', 'out'))
    strings(s['scope']['in']); strings(s['scope']['out'])
    for field in ('decisions', 'assumptions', 'blockers', 'success_criteria'):
        strings(s[field])
    t = s['team']
    shape(t, ('lead_owner', 'participating_owners'))
    participants = t['participating_owners']
    strings(participants, unique=True)
    require(all(p in candidates for p in participants), 'Unknown participant')
    require(t['lead_owner'] is None or (type(t['lead_owner']) is str and t['lead_owner'] in participants), 'Nonparticipating lead')
    shape(s['what_happens_first'], ('action', 'reason'))
    text(s['what_happens_first']['action']); text(s['what_happens_first']['reason'])
    require(type(s['requested_contributions']) is list, 'Contribution list')
    for request in s['requested_contributions']:
        shape(request, ('owner', 'request'))
        text(request['owner']); text(request['request'])
        require(request['owner'] in participants, 'Nonparticipating requested owner')
    work = s['work']
    require(type(work) is list, 'Work list')
    graph = {}
    for item in work:
        shape(item, ('id', 'objective', 'owner', 'depends_on', 'status'))
        for field in ('id', 'objective', 'owner'):
            text(item[field])
        require(item['id'] not in graph, 'Duplicate work ID')
        require(item['owner'] in participants, 'Nonparticipating work owner')
        require(item['status'] == 'planned', 'Work must be planned')
        strings(item['depends_on'], unique=True)
        graph[item['id']] = item['depends_on']
    for key, deps in graph.items():
        require(key not in deps and all(dep in graph for dep in deps), 'Unknown/self dependency')
    # Iterative topological elimination avoids Python recursion limits.
    remaining = dict(graph)
    while remaining:
        roots = {key for key, deps in remaining.items() if not any(d in remaining for d in deps)}
        require(bool(roots), 'Cyclic work graph')
        remaining = {key: deps for key, deps in remaining.items() if key not in roots}
    if status == 'ready':
        require(bool(s['scope']['in']) and bool(participants) and t['lead_owner'] in participants and bool(work) and bool(s['success_criteria']), 'Incomplete ready state')
        require(not s['blockers'] and not s['requested_contributions'], 'Ready has unresolved needs')
    elif status == 'clarify':
        require(bool(s['blockers']), 'Clarification needs concrete blocker')


def orchestrator_input(value):
    shape(value, ('initiative', 'governance', 'available_realm_owners'), ('planning_room',))
    initiative(value['initiative'])
    governance = value['governance']
    shape(governance, ('decision', 'reason'), ('next_owner',))
    text(governance['reason'])
    if 'next_owner' in governance:
        require(governance['next_owner'] == 'orchestrator', 'Governor route')
    require(value['governance']['decision'] == 'proceed', 'Governance must proceed')
    candidates = value['available_realm_owners']
    require(type(candidates) is list, 'Candidates list')
    ids = []
    for candidate in candidates:
        shape(candidate, ('owner', 'realm', 'responsibility'))
        for field in candidate:
            text(candidate[field])
        require(candidate['owner'] in OWNERS and candidate['realm'] == DOMAINS[OWNERS.index(candidate['owner'])], 'Canonical candidate mismatch')
        ids.append(candidate['owner'])
    require(len(ids) == len(set(ids)), 'Duplicate candidate')
    if 'planning_room' in value:
        room = value['planning_room']
        shape(room, ('contributions',))
        require(type(room['contributions']) is list, 'Contribution list')
        for c in room['contributions']:
            fields = ('questions', 'assumptions', 'dependencies', 'risks', 'blocking_objections')
            shape(c, ('owner', 'contribution'), fields)
            text(c['owner']); text(c['contribution'])
            require(c['owner'] in ids, 'Unknown contributor')
            for field in fields:
                if field in c: strings(c[field])


def owner_input(value, objective):
    shape(value, ('handoff', 'assignment', 'dependencies', 'approval_authority'), ('context',))
    orchestrator(value['handoff'], objective)
    require(value['handoff']['orchestration_status'] == 'ready', 'Nonready handoff')
    a = value['assignment']
    shape(a, ('canonical_domain', 'owner', 'work_id'))
    require(a['canonical_domain'] == DOMAINS[0] and a['owner'] == OWNER, 'Assignment owner/domain')
    text(a['work_id'])
    work = [w for w in value['handoff']['initiative_state']['work'] if w['id'] == a['work_id'] and w['owner'] == a['owner']]
    require(len(work) == 1, 'Assignment work ID/owner')
    deps = value['dependencies']
    require(type(deps) is list, 'Dependencies list')
    ids = []
    for dep in deps:
        shape(dep, ('id', 'satisfied', 'evidence'))
        text(dep['id']); text(dep['evidence'], empty=not dep['satisfied'])
        require(type(dep['satisfied']) is bool, 'Dependency boolean')
        ids.append(dep['id'])
    require(len(ids) == len(set(ids)) and set(ids) == set(work[0]['depends_on']), 'Dependency coverage')
    if value['approval_authority'] is not None: text(value['approval_authority'])
    if 'context' in value: text(value['context'], empty=True)


def owner_output(value, assignment):
    shape(value, ('owner_status', 'reason', 'canonical_domain', 'owner', 'work_id', 'result', 'assumptions', 'risks', 'blockers', 'routing_needs', 'next_owner'))
    status = value['owner_status']
    require(status in ('draft', 'review', 'blocked', 'clarify'), 'Owner status')
    text(value['reason'])
    require(value['canonical_domain'] == DOMAINS[0] and value['owner'] == OWNER and value['next_owner'] == 'orchestrator', 'Owner canonical identity/route')
    require(value['work_id'] == assignment['work_id'], 'Result assignment mismatch')
    r = value['result']
    shape(r, ('artifact_stage', 'content', 'checks'))
    for field in ('assumptions', 'risks', 'blockers'): strings(value[field])
    strings(r['checks'])
    require(type(value['routing_needs']) is list, 'Routing list')
    for need in value['routing_needs']:
        shape(need, ('canonical_domain', 'relationship', 'need'))
        require(need['canonical_domain'] in DOMAINS[1:] and need['relationship'] in ('primary', 'supporting'), 'Routing need identity')
        text(need['need'])
    if status in ('draft', 'review'):
        require(r['artifact_stage'] == status.upper() and not value['blockers'], 'Artifact lifecycle')
        text(r['content'])
        require(status != 'review' or bool(r['checks']), 'Review requires criterion checks')
    else:
        require(r['artifact_stage'] is None and r['content'] is None and r['checks'] == [] and bool(value['blockers']), 'Refusal lifecycle')


def supported(value):
    s = value['initiative_state']
    return (value['orchestration_status'] == 'ready' and s['team'] == {'lead_owner': OWNER, 'participating_owners': [OWNER]} and len(s['work']) == 1 and s['work'][0]['owner'] == OWNER and s['work'][0]['depends_on'] == [])


def check_unicode(value):
    if isinstance(value, str):
        for c in value:
            if 0xD800 <= ord(c) <= 0xDFFF:
                raise BoundaryError("Invalid Unicode surrogate")
    elif isinstance(value, dict):
        for k, v in value.items():
            check_unicode(k)
            check_unicode(v)
    elif isinstance(value, list):
        for v in value:
            check_unicode(v)


def parse(raw):
    require(type(raw) is str, 'YAML must be UTF-8 text')
    try:
        byte_length = len(raw.encode('utf-8'))
    except UnicodeEncodeError:
        raise BoundaryError('YAML must be valid UTF-8 text') from None
    require(byte_length <= LIMIT, 'YAML byte limit')
    try:
        depth = count = 0
        for event in yaml.parse(raw, Loader=yaml.SafeLoader):
            count += 1
            require(count <= 20000, 'YAML node limit')
            require(not isinstance(event, events.AliasEvent), 'YAML aliases unsupported')
            require(not getattr(event, 'anchor', None) and not getattr(event, 'tag', None), 'YAML anchors/tags unsupported')
            if isinstance(event, events.DocumentStartEvent):
                require(not event.explicit and not event.version and not event.tags, 'YAML document markers/directives unsupported')
            if isinstance(event, events.DocumentEndEvent):
                require(not event.explicit, 'YAML document markers unsupported')
            if isinstance(event, (events.MappingStartEvent, events.SequenceStartEvent)):
                depth += 1
                require(depth <= 32, 'YAML depth limit')
            elif isinstance(event, (events.MappingEndEvent, events.SequenceEndEvent)):
                depth -= 1
        node = yaml.compose(raw, Loader=yaml.SafeLoader)
        def decode(n):
            if isinstance(n, nodes.MappingNode):
                result = {}
                for key, value in n.value:
                    require(isinstance(key, nodes.ScalarNode) and key.tag == 'tag:yaml.org,2002:str', 'YAML keys must be strings')
                    require(key.value not in result, 'Duplicate YAML key')
                    result[key.value] = decode(value)
                return result
            if isinstance(n, nodes.SequenceNode):
                return [decode(v) for v in n.value]
            require(isinstance(n, nodes.ScalarNode), 'Unsupported YAML node')
            require(n.tag in ['tag:yaml.org,2002:' + t for t in ('str', 'null', 'bool', 'int')], 'Unsupported YAML scalar')
            scalar_yaml = yaml.serialize(n)
            try:
                return yaml.safe_load(scalar_yaml)
            except BoundaryError:
                raise
            except ValueError:
                raise BoundaryError('Invalid YAML scalar') from None
        require(isinstance(node, nodes.MappingNode), 'One YAML mapping required')
        result = decode(node)
        check_unicode(result)
        return result
    except yaml.YAMLError:
        raise BoundaryError('Malformed YAML') from None
