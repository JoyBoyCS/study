#直接输出
name1='林黛玉'
name2='薛宝钗'
name3='贾元春'
name4='贾探春'
name5='史湘云'
print('➊  '+name1)
print('➋  '+name2)
print('➌  '+name3)
print('➍  '+name4)
print('➎  '+name5)

print('列表-----------------------------------------')

#使用列表输出
lst_name=['林黛玉','薛宝钗','贾元春','贾探春','史湘云']
lst_sig=['➊ ','➋ ','➌ ','➍ ','➎ ']
for i in range(5):
    print(lst_sig[i],lst_name[i])
    
print('字典------------------------------------------')

#使用字典输出
d={'➊ ':'林黛玉','➋ ':'薛宝钗','➌ ':'贾元春','➍ ':'贾探春','➎ ':'史湘云'}
for key in d:
    print(key,d[key])

print('zip------------------------------------------')
  
#zip方式
for s,name in zip(lst_sig,lst_name):
    print(s,name)