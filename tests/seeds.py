from copy import deepcopy
import yaml

OWNER = 'professional_delivery_owner'
OBJECTIVE = 'Draft one internal release-note sentence for the fictional professional project Atlas.'
INITIATIVE = {'objective': OBJECTIVE, 'context': 'Supplied authoritative fictional fact: version 2 fixes the search typo. Use only this fact. Success: one sentence naming version 2 and the search typo fix; no testing, dates, extra changes, external actions, approval or release. Drafting permitted by project editor. One independent professional text item.'}
GOV = {'decision': 'proceed', 'reason': 'Drafting is permitted.', 'next_owner': 'orchestrator'}
PLAN = {'orchestration_status': 'ready', 'reason': 'All supplied facts suffice.', 'initiative_state': {'objective': OBJECTIVE, 'scope': {'in': ['One supplied-fact sentence'], 'out': ['Publishing and external actions']}, 'team': {'lead_owner': OWNER, 'participating_owners': [OWNER]}, 'decisions': ['One professional text item.'], 'assumptions': [], 'blockers': [], 'work': [{'id': 'actual_returned_id', 'objective': 'Draft sentence', 'owner': OWNER, 'depends_on': [], 'status': 'planned'}], 'success_criteria': ['One sentence naming version 2 and search typo fix'], 'what_happens_first': {'action': 'Draft the sentence', 'reason': 'Facts supplied'}, 'requested_contributions': []}, 'next_action': {'type': 'handoff', 'target': 'domain_owner'}}
RESULT = {'owner_status': 'review', 'reason': 'Text criteria checked; no approval or delivery.', 'canonical_domain': 'professional_delivery', 'owner': OWNER, 'work_id': 'actual_returned_id', 'result': {'artifact_stage': 'REVIEW', 'content': 'Atlas version 2 fixes the search typo.', 'checks': ['Inspected one sentence naming version 2 and the search typo fix.']}, 'assumptions': [], 'risks': ['Human acceptance remains pending.'], 'blockers': [], 'routing_needs': [], 'next_owner': 'orchestrator'}

class FixtureDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def raw(value):
    return yaml.dump(value, Dumper=FixtureDumper, sort_keys=False, allow_unicode=True)

def plan(status):
    value = deepcopy(PLAN)
    if status != 'ready':
        value['orchestration_status'] = status
        value['next_action'] = {'type': 'request_governance_clarification' if status == 'clarify' else 'convene_planning_room', 'target': 'governor' if status == 'clarify' else 'planning_room'}
        value['initiative_state']['blockers'] = ['Required fact unavailable']
        value['initiative_state']['work'] = []
        if status == 'planning':
            value['initiative_state']['requested_contributions'] = [{'owner': OWNER, 'request': 'Supply exact version and change'}]
    return value

def result(status):
    value = deepcopy(RESULT)
    value['owner_status'] = status
    if status in ('blocked', 'clarify'):
        value['blockers'] = ['The required version/change fact is unavailable']
        value['result'] = {'artifact_stage': None, 'content': None, 'checks': []}
    else:
        value['result']['artifact_stage'] = status.upper()
    return value
