class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        rule_criteria = ['type', 'color', 'name']
        rule_criteria_index = rule_criteria.index(ruleKey)
        counter = 0
        for item_list in items:
            if (ruleValue == item_list[rule_criteria_index]):
                counter += 1
        return counter