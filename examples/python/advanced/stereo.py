import cupoch as cph

limg = cph.io.read_image("../../testdata/left.png").create_gray_image()
rimg = cph.io.read_image("../../testdata/right.png").create_gray_image()
print(limg)
print(rimg)
cph.visualization.draw_geometries([limg])
params = cph.imageproc.SGMOption()
params.width = limg.width
params.height = limg.height

sgm = cph.imageproc.SemiGlobalMatching(params)
disp = sgm.process_frame(limg, rimg)
disp.linear_transform(255.0 / 127.0)
cph.visualization.draw_geometries([disp])
