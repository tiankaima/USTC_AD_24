from math import log2


def calc_dcg(rel_list: list[float], k: int) -> float:
    dcg = 0
    for i in range(k):
        dcg += (2 ** rel_list[i] - 1) / (log2(i + 2))
    return dcg


def calc_idcg(rel_list: list[float]) -> float:
    rel_list = sorted(rel_list, reverse=True)
    return calc_dcg(rel_list, len(rel_list))


def calc_ndcg(rel_list: list[float], k: int) -> float:
    dcg = calc_dcg(rel_list, k)
    idcg = calc_idcg(rel_list)
    return dcg / idcg


if __name__ == "__main__":
    A = [3, 3, 0, 2, 2, 1]
    B = [3, 3, 2, 0, 2, 1]

    print("A: {}, NDCG(A): {}".format(A, calc_ndcg(A, len(A))))
    print("B: {}, NDCG(B): {}".format(B, calc_ndcg(B, len(B))))
