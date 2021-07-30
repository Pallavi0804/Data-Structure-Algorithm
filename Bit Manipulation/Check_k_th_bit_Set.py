# Using Left SHift
def check_k_bit_set_left_shift(n,k):
    if 1<<(k-1) & n !=0:
        return "Yes"
    else:
        return "No"

# Using Right Shift
def check_k_bit_set_right_shift(n,k):
    if n>>(k-1) & 1 == 1:
        return "Yes"
    else:
        return "No"

n = 6
k = 4
print(check_k_bit_set_left_shift(n,k))
print(check_k_bit_set_right_shift(n,k))

