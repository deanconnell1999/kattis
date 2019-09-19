def binaryToDecimal(x): 
    binary = x; 
    decimal = 0;  
    base = 1;   
    length = len(binary); 
    for a in range(length - 1, -1, -1): 
        if (binary[a] == '1'):      
            decimal += base; 
        base = base * 2;
    return decimal;


num = int(input())
bin_num = bin(num).replace("0b", "")
reverse_bin = str(bin_num)[::-1]
print(binaryToDecimal(reverse_bin))