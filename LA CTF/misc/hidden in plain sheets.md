# Challenge: hidden in plain sheets

**Category:** misc

**Description:** I found this google sheets link on the internet. I'm sure it's hiding something, but I can't find anything? Can you find the flag? Choose any link (they're all the same): [Link 1](https://docs.google.com/spreadsheets/d/1OYx3lCccLKYgOvzxkRZ5-vAwCn3mOvGUvB4AdnSbcZ4/edit)&nbsp;&nbsp;&nbsp;&nbsp;[Link 2](https://docs.google.com/spreadsheets/d/17A1f0z8rmR7356fcHmHTHt3Y0JMgcHlGoflADtNXeOU/edit)&nbsp;&nbsp;&nbsp;&nbsp;[Link 3](https://docs.google.com/spreadsheets/d/1ULdm_KCOYCWuf6gqpg6tm0t-wnWySX_Bf3yUYOfZ2tw/edit)

Really fun chall that got me thinking outside the box to get the solution. Each link leads to a Google Sheets file, and when you look at it at first, it looks like there  is one sheet with nothing relevant to finding the flag. So, the first thing I did was sift around the settings and perms that I could use to find any more information. However, there were a lot of restrictions: I only had viewer access, so no editing the sheet and its properties; I did not have the ability to download it to try to bypass any restrictions to see any other contents of the sheet on my Google Drive or locally on my laptop. I was able to find information about a hidden sheet named "flag." You can find it either doing

[1]. clicking Data > Protected sheets & ranges > Show all protected ranges 

![image](https://user-images.githubusercontent.com/61215553/221341974-aba9d5ba-cfe1-4204-91ab-e1181fddd418.png)

![image](https://user-images.githubusercontent.com/61215553/221342034-9c97a5e4-0f64-4617-94ff-7ca43e108f19.png)

![image](https://user-images.githubusercontent.com/61215553/221342052-eaf62d86-8789-4282-9f37-20c3d6b3c71e.png "Hidden sheet shown")


or [2]. clicking View > Hidden sheets (1), then Show flag is listed as a greyed-out option).

![image](https://user-images.githubusercontent.com/61215553/221341829-88955cb1-1d9a-4f9a-a92c-0a6b596c6e31.png "Hidden sheet revealed")

The main tool at my disposal that I used was the Find and replace tool (shortcut is Ctrl+H). The tool allowed for me to search through all the sheets for any contents inside of them, so by playing around with it I was able to get a few characters of the flag in the flag sheet, each character seeming to be in a different cell, ranging from cells A1 to AR1 (so horizontally you can read out the flag). The caveat to using the tool was that it seems to find only the first occurrences of a character in each search, so I learned that I could specify the ranges to search through by using a filter. In the Search field of the tool, select Specific range from the drop-down menu, and on the right specify the sheet and range (i.e. flag!N1 to search a single cell in the flag sheet or Sheet1!A1:F1 to search in cells A1 to F1). With that, toying around a bit more with the tool and doing some guess andcheck, I was able to get all the characters in the flag and thus the flag itself.

**Flag:** lactf{H1dd3n_&_prOt3cT3D_5h33T5_Ar3_n31th3r}

Solved by giggsterpuku
