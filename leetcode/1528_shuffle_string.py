class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        char_list = list(s)
        zip_lists = zip(indices, char_list)
        ind_char_dict = dict(zip_lists)
        new_char_list = []
        for i in range(len(indices)):
            new_char_list.append(ind_char_dict[i])

        return "".join(new_char_list)