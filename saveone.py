import pyrealsense2 as rs
import numpy as np
import cv2

if __name__ == "__main__":
    # Configure depth and color streams
    # 配置深度和颜色流
    pipeline = rs.pipeline()
    config = rs.config()
    config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
    config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

    # Start streaming
    # 开始流式传输
    pipeline.start(config)

    frames = pipeline.wait_for_frames()
    depth_frame = frames.get_depth_frame()
    color_frame = frames.get_color_frame()

    if not depth_frame or not color_frame:
            # 将图像转换为数字数组
            # Convert images to numpy arrays
            depth_image = np.asanyarray(depth_frame.get_data())
            color_image = np.asanyarray(color_frame.get_data())
            # Apply colormap on depth image (image must be converted to 8-bit per pixel first)
            # 在深度图像上应用颜色图（必须先将图像转换为每像素 8 位）
            depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)
            # 将图像转换为数字数组
            # Convert images to numpy arrays

            cv2.imshow('color',color_image)
            cv2.imshow('depth',depth_image)
            # Stack both images horizontally
            cv2.imwrite('color1.jpg',color_image)
            cv2.imwrite('depth1.jpg',depth_image)
            cv2.waitKey(0)
            # cv2.destroyAllWindows()