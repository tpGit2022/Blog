[TOC]


FFMPEG H264和H265的转化

```
ffmpeg -i test_h264 test.hevc //.h264转265

ffmpeg -i test_h

// 感觉上面的指令有问题

ffmpeg -i 1.mp4 -c:v libx265 video_h265.mp4 // MP4的编码转化
```



VS2017 FFMPEG 配置说明

下载 FFMPEG 后目录如下:

bin 包含 dll文件 ，include 是 .h 即头文件， lib 包含 lib,def库文件

```
├─bin
│      avcodec-58.dll
│      avdevice-58.dll
│      avfilter-7.dll
│      avformat-58.dll
│      avutil-56.dll
│      ffmpeg.exe
│      ffplay.exe
│      ffprobe.exe
│      postproc-55.dll
│      swresample-3.dll
│      swscale-5.dll
│      
├─include
│  │  LICENSE
│  │  
│  ├─libavcodec
│  │      ac3_parser.h
│  │      adts_parser.h
│  │      avcodec.h
│  │      avdct.h
│  │      avfft.h
│  │      d3d11va.h
│  │      dirac.h
│  │      dv_profile.h
│  │      dxva2.h
│  │      jni.h
│  │      mediacodec.h
│  │      qsv.h
│  │      vaapi.h
│  │      vdpau.h
│  │      version.h
│  │      videotoolbox.h
│  │      vorbis_parser.h
│  │      xvmc.h
│  │      
│  ├─libavdevice
│  │      avdevice.h
│  │      version.h
│  │      
│  ├─libavfilter
│  │      avfilter.h
│  │      buffersink.h
│  │      buffersrc.h
│  │      version.h
│  │      
│  ├─libavformat
│  │      avformat.h
│  │      avio.h
│  │      version.h
│  │      
│  ├─libavutil
│  │      adler32.h
│  │      aes.h
│  │      aes_ctr.h
│  │      attributes.h
│  │      audio_fifo.h
│  │      avassert.h
│  │      avconfig.h
│  │      avstring.h
│  │      avutil.h
│  │      base64.h
│  │      blowfish.h
│  │      bprint.h
│  │      bswap.h
│  │      buffer.h
│  │      camellia.h
│  │      cast5.h
│  │      channel_layout.h
│  │      common.h
│  │      cpu.h
│  │      crc.h
│  │      des.h
│  │      dict.h
│  │      display.h
│  │      downmix_info.h
│  │      encryption_info.h
│  │      error.h
│  │      eval.h
│  │      ffversion.h
│  │      fifo.h
│  │      file.h
│  │      frame.h
│  │      hash.h
│  │      hdr_dynamic_metadata.h
│  │      hmac.h
│  │      hwcontext.h
│  │      hwcontext_cuda.h
│  │      hwcontext_d3d11va.h
│  │      hwcontext_drm.h
│  │      hwcontext_dxva2.h
│  │      hwcontext_mediacodec.h
│  │      hwcontext_qsv.h
│  │      hwcontext_vaapi.h
│  │      hwcontext_vdpau.h
│  │      hwcontext_videotoolbox.h
│  │      imgutils.h
│  │      intfloat.h
│  │      intreadwrite.h
│  │      lfg.h
│  │      log.h
│  │      lzo.h
│  │      macros.h
│  │      mastering_display_metadata.h
│  │      mathematics.h
│  │      md5.h
│  │      mem.h
│  │      motion_vector.h
│  │      murmur3.h
│  │      opt.h
│  │      parseutils.h
│  │      pixdesc.h
│  │      pixelutils.h
│  │      pixfmt.h
│  │      random_seed.h
│  │      rational.h
│  │      rc4.h
│  │      replaygain.h
│  │      ripemd.h
│  │      samplefmt.h
│  │      sha.h
│  │      sha512.h
│  │      spherical.h
│  │      stereo3d.h
│  │      tea.h
│  │      threadmessage.h
│  │      time.h
│  │      timecode.h
│  │      timestamp.h
│  │      tree.h
│  │      twofish.h
│  │      tx.h
│  │      version.h
│  │      xtea.h
│  │      
│  ├─libpostproc
│  │      postprocess.h
│  │      version.h
│  │      
│  ├─libswresample
│  │      swresample.h
│  │      version.h
│  │      
│  └─libswscale
│          swscale.h
│          version.h
│          
└─lib32
        avcodec-58.def
        avcodec.lib
        avdevice-58.def
        avdevice.lib
        avfilter-7.def
        avfilter.lib
        avformat-58.def
        avformat.lib
        avutil-56.def
        avutil.lib
        postproc-55.def
        postproc.lib
        swresample-3.def
        swresample.lib
        swscale-5.def
        swscale.lib
        

```

配置上

* VC++目录-->包含目录 填入上面的 include 目录即头文件所在的目录
* VC++目录-->库目录  填入上面的lib32 目录即lib和def所在的目录
* 链接器-->输入-->附加依赖项 填入上面lib32下所有lib文件的绝对路径


测试代码 

```
/// 测试链接 RTSP 编码格式是H.265 的流媒体

#include <iostream>
#include <stdlib.h>
#include <atlstr.h>

using namespace std;

//必须添加
#ifdef __cplusplus
extern "C" {
#endif
#include<libavformat/avformat.h>
#ifdef __cplusplus
}
#endif // __cplusplus


int read_rtsp_h265_with_ffmpeg();

int main()
{
	read_rtsp_h265_with_ffmpeg();
    std::cout << "Hello World!\n";
}

int read_rtsp_h265_with_ffmpeg() {
	AVFormatContext *pFormatCtx = NULL;
	AVDictionary *options = NULL;
	AVPacket *packet = NULL;
	//rtsp://admin:123456@192.168.123.130:554/stream1
	//char filepath[] = "rtsp://admin:123456@192.168.123.130:554/stream1";
	char filepath[] = "rtsp://192.168.1.103:8554/teststream_h265";

	//av_register_all();  //函数在ffmpeg4.0以上版本已经被废弃，所以4.0以下版本就需要注册初始函数

	av_dict_set(&options, "buffer_size", "1024000", 0); //设置缓存大小,1080p可将值跳到最大
	av_dict_set(&options, "rtsp_transport", "tcp", 0); //以tcp的方式打开,
	av_dict_set(&options, "stimeout", "5000000", 0); //设置超时断开链接时间，单位us
	av_dict_set(&options, "max_delay", "500000", 0); //设置最大时延

	pFormatCtx = avformat_alloc_context(); //用来申请AVFormatContext类型变量并初始化默认参数,申请的空间


	//打开网络流或文件流
	if (avformat_open_input(&pFormatCtx, filepath, NULL, &options) != 0)
	{
		printf("Couldn't open input stream.\n");
		return 0;
	}
	printf("视频流打开成功 \n");
	//获取视频文件信息
	if (avformat_find_stream_info(pFormatCtx, NULL) < 0)
	{
		printf("Couldn't find stream information.\n");
		return 0;
	}

	CString timeLong;
	int tns, thh, tmm, tss;
	tns = (pFormatCtx->duration) / 1000000;
	thh = tns / 3600;
	tmm = (tns % 3600) / 60;
	tss = tns % 60;

	cout << "视频流信息:\n" 
		<< "文件信息" <<  pFormatCtx->filename 
		<< "\n总长度" << thh << ":" << tmm << ":" << tss
		<<  "\n比特率" << pFormatCtx->bit_rate 
		<< "\n流信息:" 
		<< "\n帧率" << pFormatCtx->streams[0]->avg_frame_rate.num 
		<< "/" << pFormatCtx->streams[0]->avg_frame_rate.den
		<< "\n编码相关信息:\n" 
		
		<<endl;

	//查找码流中是否有视频流
	int videoindex = -1;
	unsigned i = 0;
	for (i = 0; i < pFormatCtx->nb_streams; i++)
		if (pFormatCtx->streams[i]->codec->codec_type == AVMEDIA_TYPE_VIDEO)
		{
			videoindex = i;
			break;
		}
	if (videoindex == -1)
	{
		printf("Didn't find a video stream.\n");
		return 0;
	}

	packet = (AVPacket *)av_malloc(sizeof(AVPacket)); // 申请空间，存放的每一帧数据 （h264、h265）


	FILE *fpSave;
	fpSave = fopen("geth265_test.h265", "wb");

	//这边可以调整i的大小来改变文件中的视频时间,每 +1 就是一帧数据
	for (i = 0; i < 200; i++)
	{
		if (av_read_frame(pFormatCtx, packet) >= 0)
		{
			if (packet->stream_index == videoindex)
			{
				fwrite(packet->data, 1, packet->size, fpSave);
			}
			av_packet_unref(packet);
		}
	}

	fclose(fpSave);
	av_free(packet);
	avformat_close_input(&pFormatCtx);
}
```


错误 [hevc @ 0x7ffea0a9c800] Could not find ref with POC 15

```
工作中音视频推流遇到H265编码的rtp包，发现rtmp-flv不支持，就想到把h265，解码-编码为h264，然后再推上去，结果在编解码的时候发现，h265不停打印：
[hevc @ 0x7ffea0a9c800] Could not find ref with POC 76
[hevc @ 0x7ffea0a9c800] Could not find ref with POC 15
。
。
。
百思不得，然后一个一个试，结果发现是：
当输入跟不上编解码的时候就会打印这些，假如说你能控制输入，当你把输入速率调低，比如10p/s那么就会出现上述现象，当调为30p/s就不会出现，所以关键是输入，至于怎么解决这个问题，根据不同的情况解决就好
```

中光项目代码

The C++ Standard Library forbids macroizing keywords. Enable warning C4005 to find the forbidden macr

预处理需要添加 

属性--> C/C++--->预处理器---> 预处理定义添加 _XKEYCHECK_H
_XKEYCHECK_H



设置关键帧信息

 ffmpeg -i 15s.mp4 -g 10 gop10_15s.mp4

查看关键帧信息

ffprobe -show_frames  gop10_15s.mp4

ffprobe -show_frames -select_streams v   gop10_15s.mp4


关键帧，IDR的区别 

IDR是关键帧  ，关键帧不一定是IDR

```
[FRAME]
media_type=video
stream_index=0
key_frame=0
pkt_pts=25200
pkt_pts_time=0.280000
pkt_dts=25200
pkt_dts_time=0.280000
best_effort_timestamp=25200
best_effort_timestamp_time=0.280000
pkt_duration=N/A
pkt_duration_time=N/A
pkt_pos=N/A
pkt_size=1109
width=960
height=1900
pix_fmt=yuvj420p
sample_aspect_ratio=N/A
pict_type=P
coded_picture_number=0
display_picture_number=0
interlaced_frame=0
top_field_first=0
repeat_pict=0
color_range=pc
color_space=bt709
color_primaries=bt709
color_transfer=bt709
chroma_location=unspecified
[/FRAME]
```

pict_type
key_frame


ffprobe.c

```
static void show_frame(WriterContext *w, AVFrame *frame, AVStream *stream,
                       AVFormatContext *fmt_ctx)
```

```
print_int("key_frame",              frame->key_frame);

print_fmt("pict_type",              "%c", av_get_picture_type_char(frame->pict_type));
```


# 参考资料

1. [利用ffmpeg和opencv进行视频的解码播放](https://blog.csdn.net/JasonDing1354/article/details/41212425)