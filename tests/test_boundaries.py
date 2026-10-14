import unittest

from olympus.boundaries import BoundaryError, parse


class ParserTests(unittest.TestCase):
    def test_restricted_single_mapping(self):
        self.assertEqual(parse('reason: "a: b"\nchecks: []\n'), {'reason': 'a: b', 'checks': []})
        for raw in ['```yaml\na: b\n```', 'commentary\na: b', 'a: b\na: c', 'a: {b: c, b: d}', '---\na: b\n---\na: c', 'a: !!str b', 'a: &x [b]\nb: *x', '? [a, b]\n: c', '[a, b]', 'a: 2026-01-01', 'a: .nan', '%YAML 1.1\n---\na: b']:
            with self.subTest(raw=raw), self.assertRaises(BoundaryError):
                parse(raw)
        for raw in ['a: ' + 'x' * 1048576, 'a: ' + '[' * 35 + 'x' + ']' * 35]:
            with self.assertRaises(BoundaryError):
                parse(raw)


class GovernorTests(unittest.TestCase):
    def test_governor_input_output_contract(self):
        from olympus.boundaries import governor, initiative
        from seeds import GOV
        initiative({'objective': ''}, allow_empty=True)
        governor(GOV)
        for decision in ('stop', 'clarify'):
            governor({'decision': decision, 'reason': 'Missing intent', 'next_owner': None})
        for value in [{**GOV, 'next_owner': 'Hermes'}, {**GOV, 'reason': ''}, {**GOV, 'extra': 1}, {**GOV, 'decision': True}]:
            with self.assertRaises(BoundaryError):
                governor(value)
        for value in [{'objective': None}, {'objective': '', 'extra': ''}, {'objective': 'x', 'context': []}]:
            with self.assertRaises(BoundaryError):
                initiative(value)


if __name__ == '__main__':
    unittest.main()
