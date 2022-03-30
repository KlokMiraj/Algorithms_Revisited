class 2D_aray:
    def solution(self,matrix,target):
            match={}
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    match=matrix[i][j]-target
                    if match == 0:
                        return True
            return False