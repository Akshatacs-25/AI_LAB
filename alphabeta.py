
def alphabeta(depth, node, alpha, beta, maximizing, values):
    if depth == 3:
        return values[node]

    if maximizing:
        best = -999
        for i in range(2):
            val = alphabeta(depth+1, node*2+i, alpha, beta,
                            False, values)
            best = max(best, val)
            alpha = max(alpha, best)

            if alpha >= beta:
                break
        return best

    else:
        best = 999
        for i in range(2):
            val = alphabeta(depth+1, node*2+i, alpha, beta,
                            True, values)
            best = min(best, val)
            beta = min(beta, best)

            if alpha >= beta:
                break
        return best


values = [3, 5, 6, 9, 1, 2, 0, -1]

result = alphabeta(0, 0, -999, 999, True, values)

print("Optimal value:", result)
