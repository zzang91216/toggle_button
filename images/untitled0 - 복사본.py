from PIL import Image

a = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60']
b = ['1','2','3','4']

index1 = []
index2 = [30, 39, 41, 54, 55, 57, 58]
index3 = [11, 50, 51, 52, 53, 56]
index4 = [12, 13, 21, 22, 23, 24, 25, 44, 45]
index5 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 15, 16, 17, 18, 19, 20, 26, 27, 28, 29, 31, 32, 33, 34, 35, 36, 37, 38, 40, 42, 43, 46, 47, 48, 49, 59]

new1 = Image.new('RGBA',(1100, 6000))
new_image = Image.new('RGBA',(1100, 6000), (247,247,247))


for i in range(len(index2)):
    imname = "./" + a[index2[i]] + b[0] + ".png"
    image1 = Image.open(imname).convert("RGBA")
    imname = "./" + a[index2[i]] + b[1] + ".png"
    image2 = Image.open(imname).convert("RGBA")
    
    image3 = Image.new('RGBA',(500, 250), (230,230,230))
    new_image.paste(image3,(int(600*(i%2)),int(6.75+300*(i//2))))
    
    image3 = Image.new('RGBA',(190, 190), (240,200,160))
    new_image.paste(image3,(280+int(600*(i%2)),int(36.75+300*(i//2))))
    
    new1.paste(image1,(int(50+600*(i%2)),int(36.75+300*(i//2))))
    new1.paste(image2,(int(300+600*(i%2)),int(36.75+300*(i//2))))
    
im3 = Image.alpha_composite(new_image, new1)
im3.save("./perresult1.png", 'png')


new1 = Image.new('RGBA',(1100, 6000))
new_image = Image.new('RGBA',(1100, 6000), (247,247,247))
for i in range(len(index5)):
    imname = "./" + a[index5[i]] + b[0] + ".png"
    image1 = Image.open(imname).convert("RGBA")
    imname = "./" + a[index5[i]] + b[1] + ".png"
    image2 = Image.open(imname).convert("RGBA")
    
    image3 = Image.new('RGBA',(500, 250), (230,230,230))
    new_image.paste(image3,(int(600*(i%2)),int(6.75+300*(i//2))))
    
    image3 = Image.new('RGBA',(190, 190), (240,160,160))
    new_image.paste(image3,(30+int(600*(i%2)),int(36.75+300*(i//2))))
    
    new1.paste(image1,(int(50+600*(i%2)),int(36.75+300*(i//2))))
    new1.paste(image2,(int(300+600*(i%2)),int(36.75+300*(i//2))))
    
im3 = Image.alpha_composite(new_image, new1)
im3.save("./perresult4.png", 'png')



new1 = Image.new('RGBA',(1100, 6000))
new_image = Image.new('RGBA',(1100, 6000), (247,247,247))
for i in range(len(index4)):
    imname = "./" + a[index4[i]] + b[0] + ".png"
    image1 = Image.open(imname).convert("RGBA")
    imname = "./" + a[index4[i]] + b[1] + ".png"
    image2 = Image.open(imname).convert("RGBA")
    
    image3 = Image.new('RGBA',(500, 250), (230,230,230))
    new_image.paste(image3,(int(600*(i%2)),int(6.75+300*(i//2))))
    
    image3 = Image.new('RGBA',(190, 190), (240,200,160))
    new_image.paste(image3,(30+int(600*(i%2)),int(36.75+300*(i//2))))
    
    new1.paste(image1,(int(50+600*(i%2)),int(36.75+300*(i//2))))
    new1.paste(image2,(int(300+600*(i%2)),int(36.75+300*(i//2))))
    
im3 = Image.alpha_composite(new_image, new1)
im3.save("./perresult3.png", 'png')


new1 = Image.new('RGBA',(1100, 6000))
new_image = Image.new('RGBA',(1100, 6000), (247,247,247))
for i in range(len(index3)):
    imname = "./" + a[index3[i]] + b[0] + ".png"
    image1 = Image.open(imname).convert("RGBA")
    imname = "./" + a[index3[i]] + b[1] + ".png"
    image2 = Image.open(imname).convert("RGBA")
    
    image3 = Image.new('RGBA',(500, 250), (230,230,230))
    new_image.paste(image3,(int(600*(i%2)),int(6.75+300*(i//2))))
    
    new1.paste(image1,(int(50+600*(i%2)),int(36.75+300*(i//2))))
    new1.paste(image2,(int(300+600*(i%2)),int(36.75+300*(i//2))))
    
im3 = Image.alpha_composite(new_image, new1)
im3.save("./perresult2.png", 'png')

new1 = Image.new('RGBA',(1100, 6000))
new_image = Image.new('RGBA',(1100, 6000), (247,247,247))
for i in range(len(index1)):
    imname = "./" + a[index1[i]] + b[0] + ".png"
    image1 = Image.open(imname).convert("RGBA")
    imname = "./" + a[index1[i]] + b[1] + ".png"
    image2 = Image.open(imname).convert("RGBA")
    
    image3 = Image.new('RGBA',(500, 250), (230,230,230))
    new_image.paste(image3,(int(600*(i%2)),int(6.75+300*(i//2))))
    
    new1.paste(image1,(int(50+600*(i%2)),int(36.75+300*(i//2))))
    new1.paste(image2,(int(300+600*(i%2)),int(36.75+300*(i//2))))
    
im3 = Image.alpha_composite(new_image, new1)
im3.save("./perresult0.png", 'png')