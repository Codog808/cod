import ctools
def main():
    data = ctools.wopen("day8.d")
    trees, visible_total = [list(map(int, line)) for line in data.strip().split("\n")], 0
    scenic_score_max = 0
    print(trees)
    for row in range(len(trees)):
        for col in range(len(trees[0])):
            
            tree, visible = trees[row][col], False
            # U, D, L, R = 0, 0, 0, 0
            # find the highest possible score, not the tree with the highest score.
            score = 1

            for l in range(col-1, -1, -1):
                # L += 1
                if trees[row][l] >= tree:
                    score *= col - l
                    break
            else:
                # L +=1
                score *= col
                visible = True

            for r in range(col+1, len(trees[0])):
                # R += 1
                if trees[row][r] >= tree:
                    score *= r - col 
                    break
            else:
                # R += 1
                score *= len(trees[0])-1 - col
                visible = True

            for u in range(row-1, -1, -1):
                # U += 1
                if trees[u][col] >= tree:
                    score *= row - u
                    break
            else:
                # U += 1
                score *= row
                visible = True

            for d in range(row+1, len(trees)):
                # D += 1
                if trees[d][col] >= tree:
                    score *= d - row
                    break
            else:
                # D += 1
                score *= len(trees)-1 - row
                visible = True

            if visible:
                visible_total += 1
            # print(L, R, U, D)
            # scenic_local_total = L * R * U * D
            # print(scenic_local_total)
            # scenic_score.append(scenic_local_total)
            scenic_score_max = max(scenic_score_max, score)
    print(scenic_score_max)
    print(visible_total)
    print("success")

def sol():
    with open("day8.d") as file:
        trees, visibles, max_score = [list(map(int, line)) for line in file.read().splitlines()], 0, 0
        trees = [list(map(int, line)) for line in test_input.strip().split("\n")]
        print(trees)
        for row in range(len(trees)):
            for col in range(len(trees[0])):
                tree, visible, score = trees[row][col], False, 1

                for i in range(col+1, len(trees[0])):
                    if trees[row][i] >= tree:
                        score *= i - col
                        break
                else:
                    score *= len(trees[0]) - 1 - col
                    visible = True

                for i in range(col-1, -1, -1):
                    if trees[row][i] >= tree:
                        score *= col - i
                        break
                else:
                    score *= col
                    visible = True

                for i in range(row+1, len(trees)):
                    if trees[i][col] >= tree:
                        score *= i - row
                        break
                else:
                    score *= len(trees) - 1 - row
                    visible = True

                for i in range(row-1, -1, -1):
                    if trees[i][col] >= tree:
                        score *= row - i
                        break
                else:
                    score *= row
                    visible = True

                if visible:
                    visibles += 1

                max_score = max(max_score, score)
    return visibles, max_score


if __name__ == "__main__":
    main()
    # print(sol())
