from copy import deepcopy
import unittest
from seeds import *
from olympus.boundaries import BoundaryError


class OwnerTests(unittest.TestCase):
    def test_assignment_and_lifecycle_boundaries(self):
        from olympus.boundaries import owner_input, owner_output, orchestrator_input, OWNERS, DOMAINS
        candidates = [{'owner': o, 'realm': d, 'responsibility': 'Supplied outcome contract'} for o, d in zip(OWNERS, DOMAINS)]
        oi = {'initiative': INITIATIVE, 'governance': GOV, 'available_realm_owners': candidates}
        orchestrator_input(oi)
        for change in ({'available_realm_owners': candidates + [candidates[0]]}, {'governance': {**GOV, 'decision': 'stop', 'next_owner': None}}, {'planning_room': {'contributions': [{'owner': 'unknown', 'contribution': 'fake'}]}}):
            with self.assertRaises(BoundaryError): orchestrator_input({**oi, **change})
        assignment = {'canonical_domain': 'professional_delivery', 'owner': OWNER, 'work_id': 'actual_returned_id'}
        value = {'handoff': PLAN, 'assignment': assignment, 'dependencies': [], 'approval_authority': 'Project editor', 'context': 'fact'}
        owner_input(value, OBJECTIVE)
        for change in ({'assignment': {**assignment, 'work_id': 'fixture_id'}}, {'assignment': {**assignment, 'owner': 'Apollo'}}, {'assignment': {**assignment, 'canonical_domain': 'Work'}}, {'dependencies': [{'id': 'unknown', 'satisfied': True, 'evidence': 'x'}]}, {'approval_authority': ''}):
            with self.assertRaises(BoundaryError): owner_input({**value, **change}, OBJECTIVE)
        for status in ('draft', 'review', 'blocked', 'clarify'):
            owner_output(result(status), assignment)
        mutations = [lambda r: r.update(extra=1), lambda r: r.update(next_owner='Hermes'), lambda r: r.update(work_id='wrong'), lambda r: r.update(owner='Apollo'), lambda r: r['result'].update(artifact_stage='APPROVED'), lambda r: r['result'].update(checks=[]), lambda r: r.update(blockers=['bad']), lambda r: r.update(routing_needs=[{'canonical_domain': 'Work', 'relationship': 'primary', 'need': 'x'}])]
        for mutate in mutations:
            r = deepcopy(RESULT); mutate(r)
            with self.subTest(r=r), self.assertRaises(BoundaryError): owner_output(r, assignment)
        for field, replacement in [('content', 'hidden artifact'), ('artifact_stage', 'DRAFT'), ('checks', ['unperformed'])]:
            r = result('blocked'); r['result'][field] = replacement
            with self.assertRaises(BoundaryError): owner_output(r, assignment)
