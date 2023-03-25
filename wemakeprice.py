# -*- coding: utf-8 -*-

class Preprocessor:
    """
    A class for preprocessing string-value
    """
    @staticmethod
    def remove_whitespace(s: str, is_ignore_case=True) -> str:
        s = s.replace(" ", "")
        s = s.replace("\t", "")
        s = s.replace("\n", "")
        return s.upper() if is_ignore_case else s

    @staticmethod
    def check_dup(s: str) -> str:
        dup = ''
        dup_cnt = 0

        for i in range(len(s) - 1):
            for j in range(i + 2, len(s) + 1):
                n_dup = s[i:j]
                n_dup_cnt = s.count(n_dup)

                # (!) 2개 이상 + 현재 중복 문자열보다 더 긴 경우
                if n_dup_cnt > 1 and len(n_dup) > len(dup):
                    dup = n_dup
                    dup_cnt = n_dup_cnt
        return dup, dup_cnt

    @staticmethod
    def remove_dup(s: str, dup: str, dup_cnt: int) -> str:
        rev_s = s[::-1]
        rev_dup = dup[::-1]

        # (!) 이어진 문자가 중복되는 경우 제외 고려
        rev_s = rev_s.replace(rev_dup, "/", dup_cnt - 1)
        return rev_s[::-1]

def solution(s):
    # (!) 대소문자 변경
    s = Preprocessor.remove_whitespace(s, is_ignore_case=True)

    while True:
        dup, dup_cnt = Preprocessor.check_dup(s)

        # (!) 더 이상 조건 해당 중복 없는 경우
        if not dup_cnt:
            return s.replace("/", "")

        s = Preprocessor.remove_dup(s, dup, dup_cnt)

s = "아 너무 좋아요 좋아요 너무너무너좋아요좋아요무"
print(solution(s))