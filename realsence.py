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
    try:
        while True:
            # Wait for a coherent pair of frames: depth and color
            # 等待一对连贯的帧：深度和颜色
            frames = pipeline.wait_for_frames()
            depth_frame = frames.get_depth_frame()
            color_frame = frames.get_color_frame()
            if not depth_frame or not color_frame:
                continue
            # 将图像转换为数字数组
            # Convert images to numpy arrays

            depth_image = np.asanyarray(depth_frame.get_data())

            color_image = np.asanyarray(color_frame.get_data())

            # Apply colormap on depth image (image must be converted to 8-bit per pixel first)
            # 在深度图像上应用颜色图（必须先将图像转换为每像素 8 位）
            
            depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)

            # Stack both images horizontally
            cv2.imwrite('color1.jpg',color_image)
            cv2.imwrite('depth1.jpg',depth_image)
            # 水平堆叠两个图像
            images = np.hstack((color_image, depth_colormap))

            # Show images
            # 显示图片
            cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
            cv2.imshow('RealSense', images)
            key = cv2.waitKey(1)
            # Press esc or 'q' to close the image window
            if key & 0xFF == ord('q') or key == 27:
                cv2.destroyAllWindows()
                break
    finally:
        # Stop streaming
        pipeline.stop()
