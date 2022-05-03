import bisect

def boundedSquareSum(a, b, lower, upper):
   a = [n**2 for n in a]
   b = [n**2 for n in b]

   shorter, longer = [a, b] if len(a) < len(b) else [b, a]
   shorter = sorted(shorter)

   num_pairs = 0
   for numA in longer:
      # The index of the smallest element that is >= lower - numA
      min_idx = bisect.bisect_left(shorter, lower - numA)
      # The index of the largest element that is <= upper - numA
      max_idx = bisect.bisect_right(shorter, upper - numA)
      # All values between these indices are valid
      num_pairs += max(max_idx - min_idx, 0)

   return num_pairs

def boundedSquareSum2(a, b, lower, upper):
    m = len(a)
    n = len(b)
    a = [n**2 for n in a]
    b = [n**2 for n in b]
    a.sort()
    b.sort()
    ans = 0
    left, right = n - 1, n - 1
    for i in range(m):
        # left + 1: the leftmost pointer that all b[k]^2 + a[i]^2 >= lower when k > left + 1
        # when i get larger, a[i]^2 get larger, so b[k] should be smaller to satisfy the limit
        # so the leftmost will be samller, so keep left--
        while left >= 0 and a[i] + b[left] >= lower:
            left -= 1
        # right: the rightmost pointer that all b[k]^2 + a[i]^2 <= upper when k <= right
        # when i get larger, a[i]^2 get larger, so b[k] should be smaller
        # so the rightmost will be smaller
        while right >= 0 and a[i] + b[right] > upper:
            right -= 1
        # the b[k] that k in interval [left + 1, right] satisfy the limitation
        # lower <= b[k]^2 + a[i]^2 <= upper
        if right > left:
            ans += right - left
    return ans

def solution1():
     a = [3, -1, 9]
     b = [100, 5, -2]
     lower = 7
     upper = 99
     ans = boundedSquareSum(a, b, lower, upper)
     assert ans== 4, 'the return {} should be 5.'.format(ans)
     ans = boundedSquareSum2(a, b, lower, upper)
     assert ans== 4, 'the return {} should be 5.'.format(ans)
     print('*** >>> passed solution for boundedSquareSum')


if __name__ == '__main__':
    print("start test")
    solution1()
    print('end test')
