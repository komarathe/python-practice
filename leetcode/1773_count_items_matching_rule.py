# Refer: https://leetcode.com/problems/count-items-matching-a-rule/

# You are given an array items, where each items[i] = [typei, colori, namei]
# describes the type, color, and name of the ith item. You are also given a
# rule represented by two strings, ruleKey and ruleValue.
#
# The ith item is said to match the rule if one of the following is true:
#
# ruleKey == "type" and ruleValue == typei.
# ruleKey == "color" and ruleValue == colori.
# ruleKey == "name" and ruleValue == namei.
# Return the number of items that match the given rule.

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        rule_criteria = ['type', 'color', 'name']
        rule_criteria_index = rule_criteria.index(ruleKey)
        counter = 0
        for item_list in items:
            if (ruleValue == item_list[rule_criteria_index]):
                counter += 1
        return counter
