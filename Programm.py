in_file =open("sample_input.txt","r")
out_file = open("output.txt","w+")
goodies={}
out_list=[]
for f in in_file:
    toRead_index_price=f.index(":")
    print(f[toRead_index_price+1:].strip())
    print(f[:toRead_index_price])
    goodies[f[:toRead_index_price]]=f[toRead_index_price+1:].strip()
print(goodies) 
single_prices=list(goodies.values())


single_prices=[int(i)for i in single_prices]
single_prices.sort(reverse=True)
print(single_prices)
num_of_employees=int(input("Enter number of employees: "))
leng_considered=(len(single_prices)-num_of_employees)

print(leng_considered)

for i in range(leng_considered):
    max_price=single_prices[i]
    min_price=single_prices[num_of_employees+i]
    if i == 0:
        diff=max_price-min_price
        idx_choosen=i
    elif (max_price-min_price)<diff:
        diff=max_price-min_price
        idx_choosen=i

choosen_prices=single_prices[idx_choosen:num_of_employees+idx_choosen]
diff=max(choosen_prices)-min(choosen_prices)
print("diff",diff)

cnt=0
for key,value in goodies.items():
    single_prices[cnt]
    print(value)
    if int(value)in choosen_prices and cnt<num_of_employees:
        str1=key+": "+value
        out_list.append(str1)
        cnt+=1
        print(str1)
out_file.write("The goodies selected for distribution: ")

out_file.write("\n")

for i in out_list:
    out_file.write(i)
    out_file.write("\n")
out_file.write("And the difference between the chosen goodie with highest price and the lowest price is "+str(diff))

in_file.close()
out_file.close()