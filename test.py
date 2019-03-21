# coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    i = values.index(min(values))
    a = [0 for j in range(n)]
    a[i] = 1
    k = i + 1
    while k % n != i:
        j = 1
        if values[k % n] <= values[(k - 1) % n] and values[k % n] <= values[(k + 1) % n]:
            a[k % n] = 1
        elif values[k % n] > values[(k - 1) % n] and values[k % n] <= values[(k + 1) % n]:
            a[k % n] = a[(k - 1) % n] + 1
        else:
            while values[(k + j + 1) % n] < values[(k + j) % n]:
                j += 1
            jj = j
            a[(k + j) % n] = 1
            while jj > 0:
                a[(k + jj - 1) % n] += a[(k + jj) % n] + 1
                jj -= 1
            if values[k%n]>values[(k-1)%n]:
                a[k % n] = max(a[(k + 1) % n], a[(k - 1) % n]) + 1
        k += j
    ans=sum(a)
    print(ans)

    #
#
# # coding=utf-8
# # 本题为考试多行输入输出规范示例，无需提交，不计分。
# import sys
# if __name__ == "__main__":
#     # 读取第一行的n
#     while True:
#         n = int(sys.stdin.readline().strip())
#         m = int(sys.stdin.readline().strip())
#         line = sys.stdin.readline().strip()
#         values = list(map(int, line.split()))
#         r = max(values)
#         l = 0
#         while True:
#             mid=(l+r)/2
#             num = 0
#             for li in values:
#                 num += li // mid
#             if num >= m:
#                 if r - mid <= 0.001:
#                     ans = round(mid, 2)
#                     print(ans)
#                     break
#                 else:
#                     l=mid
#             else:
#                 r=mid


# #         j = values.index(min(values))
# #         k = (j + 1) % num
# #         a = [0 for ii in range(num)]
#         a[j] = 1
#         while k % num != j:
#             if values[k % num] > values[(k - 1) % num] or values[k % num] > values[(k + 1) % num]:
#                 pass
#     print(ans)

# coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys

# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     for i in range(n):
#         s = sys.stdin.readline().strip()
#         s1 = list(s)
#         flag2 = 0
#         flag3 = 0
#         if len(s1) < 3:
#             print(''.join(s1))
#         else:
#             k = 0
#             for j in range(2, len(s1)):
#                 if s1[j - k - 2] == s1[j - k - 1] and s1[j - k] == s1[j - k - 1]:
#                     s1.pop(j - k)
#                     k += 1
#
#             if len(s1) > 3:
#                 k = 0
#                 for j in range(3, len(s1)):
#                     if s1[j - 3 - k] == s1[j - 2 - k] and s1[j - 1 - k] == s1[j - k]:
#                         s1.pop(j - k)
#         print(''.join(s1))
# # coding=utf-8
# # 本题为考试多行输入输出规范示例，无需提交，不计分。
# import sys
#
# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     s1 = sys.stdin.readline().strip().split()
#     s2 = sys.stdin.readline().strip().split()
#     a = list(map(int, s1))
#     b = list(map(int, s2))
#     a.sort()
#     b.sort()
#     ans = 0
#     suma = 0
#     sumb = 0
#     i = 0
#     while len(a) != 0 or len(b) != 0:
#         if i % 2 == 0:
#             if len(a) != 0 and len(b) != 0:
#                 if a[-1] > b[-1]:
#                     suma += a.pop()
#                 else:
#                     b.pop()
#             elif len(a) == 0 and len(b) != 0:
#                 b.pop()
#             elif len(a) != 0 and len(b) == 0:
#                 suma += a.pop()
#         else:
#             if len(a) != 0 and len(b) != 0:
#                 if a[-1] < b[-1]:
#                     sumb += b.pop()
#                 else:
#                     a.pop()
#             elif len(a) == 0 and len(b) != 0:
#                 sumb += b.pop()
#             elif len(a) != 0 and len(b) == 0:
#                 a.pop()
#         i += 1
#     ans = suma - sumb
#     print(ans)
