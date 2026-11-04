"""Offline repository checks; these do not evaluate prompts or invoke agents."""

import json
from pathlib import Path
import re
import unittest
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
DOMAINS = {
    "professional_delivery", "research_learning", "personal_life",
    "systems_automation", "experimentation", "creative_media",
}


class RepositoryTests(unittest.TestCase):
    def test_domain_and_owner_files_match_theme(self):
        domains = {p.stem for p in (ROOT / "config/domains").glob("*.md")}
        owners = {p.stem for p in (ROOT / "config/domain_owners").glob("*.md")}
        theme = (ROOT / "config/theme.yaml").read_text()
        themed = set(re.findall(r"^  ([a-z_]+):$", theme, re.MULTILINE))
        self.assertEqual(domains, DOMAINS)
        self.assertEqual(owners, domains)
        self.assertEqual(themed, domains)

    def test_contract_identity_and_domain_fields(self):
        fields = {"canonical_domain", "display_name", "theme_owner", "primary_outcome", "owns",
                  "does_not_own", "lead_when", "collaborates_when", "returns"}
        for domain in sorted(DOMAINS):
            with self.subTest(domain=domain):
                text = (ROOT / "config/domains" / f"{domain}.md").read_text()
                block = re.search(r"```yaml\n(.*?)\n```", text, re.DOTALL)
                if block is None:
                    self.fail(f"Missing YAML contract: {domain}")
                    continue
                keys = set(re.findall(r"^([a-z_]+):", block.group(1), re.MULTILINE))
                self.assertEqual(keys, fields)
                self.assertIn(f"canonical_domain: {domain}", block.group(1))
                owner = (ROOT / "config/domain_owners" / f"{domain}.md").read_text()
                self.assertTrue(owner.startswith("# Canonical role: domain_owner"))
                self.assertIn(f"`{domain}_owner`", owner)

    def test_retained_validation_records_are_valid_json(self):
        paths = list((ROOT / "docs/validation").glob("*.json"))
        self.assertTrue(paths)
        for path in paths:
            with self.subTest(path=path.name):
                self.assertIsInstance(json.loads(path.read_text()), dict)

    def test_documentation_local_links_resolve(self):
        paths = [ROOT / "README.md", ROOT / "CONTRIBUTING.md", ROOT / "SECURITY.md"]
        paths += list((ROOT / "docs").rglob("*.md"))
        for path in paths:
            for target in re.findall(r"\]\(([^)]+)\)", path.read_text()):
                if "://" in target or target.startswith(("#", "mailto:")):
                    continue
                target = unquote(target.split("#", 1)[0])
                if target:
                    with self.subTest(path=str(path.relative_to(ROOT)), target=target):
                        self.assertTrue((path.parent / target).exists())


if __name__ == "__main__":
    unittest.main()
