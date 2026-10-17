from copy import deepcopy
import unittest
from seeds import PLAN, OBJECTIVE, OWNER, plan
from olympus.boundaries import BoundaryError


class PlanTests(unittest.TestCase):
    def validate(self, value):
        from olympus.boundaries import orchestrator
        return orchestrator(value, OBJECTIVE)

    def test_status_routes_nested_fields_graphs(self):
        self.validate(PLAN)
        self.validate(plan('planning'))
        self.validate(plan('clarify'))
        mutations = [lambda p: p.update(extra=1), lambda p: p['next_action'].update(target='Apollo'), lambda p: p['initiative_state'].update(objective='broader'), lambda p: p['initiative_state']['scope'].update(extra=[]), lambda p: p['initiative_state']['team'].update(lead_owner='Apollo'), lambda p: p['initiative_state']['team']['participating_owners'].append(OWNER), lambda p: p['initiative_state']['work'][0].update(status='done'), lambda p: p['initiative_state']['work'][0].update(depends_on=['unknown']), lambda p: p['initiative_state']['work'][0].update(depends_on=['actual_returned_id']), lambda p: p['initiative_state']['work'][0].update(owner='research_learning_owner'), lambda p: p['initiative_state'].update(blockers=['unresolved']), lambda p: p['initiative_state'].update(success_criteria=[]), lambda p: p['initiative_state'].update(requested_contributions=[{'owner': OWNER, 'request': 'fact'}]), lambda p: p['initiative_state']['what_happens_first'].update(action='')]
        for mutate in mutations:
            p = deepcopy(PLAN)
            mutate(p)
            with self.subTest(p=p), self.assertRaises(BoundaryError):
                self.validate(p)
        for kind in ('duplicate', 'cycle', 'unknown', 'self'):
            p = deepcopy(PLAN)
            w = p['initiative_state']['work']
            w.append({**w[0], 'id': 'second', 'depends_on': []})
            if kind == 'duplicate': w[1]['id'] = w[0]['id']
            if kind == 'cycle': w[0]['depends_on'], w[1]['depends_on'] = ['second'], [w[0]['id']]
            if kind == 'unknown': w[1]['depends_on'] = ['absent']
            if kind == 'self': w[1]['depends_on'] = ['second']
            with self.subTest(kind=kind), self.assertRaises(BoundaryError): self.validate(p)

    def test_valid_unsupported_is_not_invalid_or_trimmed(self):
        from olympus.boundaries import supported
        self.assertTrue(supported(PLAN))
        for kind in ('two', 'prerequisite', 'participant', 'other'):
            p = deepcopy(PLAN)
            s = p['initiative_state']
            if kind in ('two', 'prerequisite'):
                s['work'].append({**s['work'][0], 'id': 'second', 'depends_on': [] if kind == 'two' else ['actual_returned_id']})
            elif kind == 'participant': s['team']['participating_owners'].append('research_learning_owner')
            else:
                s['team'] = {'lead_owner': 'personal_life_owner', 'participating_owners': ['personal_life_owner']}
                s['work'][0]['owner'] = 'personal_life_owner'
            self.validate(p)
            self.assertFalse(supported(p))
