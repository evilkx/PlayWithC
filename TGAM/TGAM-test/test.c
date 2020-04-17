#include <stdlib.h>
#include <stdio.h>
 
#include "thinkgear.h"
 
void wait() 
{
    printf( "\n" );
    printf( "Press the ENTER key...\n" );
    fflush( stdout );
    getc( stdin );
}
 
/**
 * Program which prints ThinkGear EEG_POWERS values to stdout.
 */
int main( void ) {
 
    char *comPortName = NULL;
    int   dllVersion = 0; //动态库版本
    int   connectionId = 0;//连接ID
    int   packetsRead = 0; //包数量
    int   errCode = 0; //错误码
 
    /* Print driver version number */
    dllVersion = TG_GetDriverVersion();
    printf( "ThinkGear DLL version: %d\n", dllVersion ); //打印当前动态库版本
 
    /* Get a connection ID handle to ThinkGear */
    connectionId = TG_GetNewConnectionId(); //获取连接ID 跟文件描述符类似的功能
    if( connectionId < 0 ) {
        fprintf( stderr, "ERROR: TG_GetNewConnectionId() returned %d.\n", 
                connectionId );
        wait();
        exit( EXIT_FAILURE );
    }
    /* Set/open stream (raw bytes) log file for connection */
    // 原始数据日志 用于高级分析
    errCode = TG_SetStreamLog( connectionId, "streamLog.txt" );
    if( errCode < 0 ) {
        fprintf( stderr, "ERROR: TG_SetStreamLog() returned %d.\n", errCode );
        wait();
        exit( EXIT_FAILURE );
    }
    /* Set/open data (ThinkGear values) log file for connection */
    //ThinkGear数据日志 一种动态库已经封装好的数据 
    errCode = TG_SetDataLog( connectionId, "dataLog.txt" );
    if( errCode < 0 ) {
        fprintf( stderr, "ERROR: TG_SetDataLog() returned %d.\n", errCode );
        wait();
        exit( EXIT_FAILURE );
    }
    /* Attempt to connect the connection ID handle to serial port "COM5" */
    comPortName = "\\\\.\\COM6"; //这个是要连接的COM端口 这个在那个计算机管理工具里面看 里面的COM端口多少这里就多少
    errCode = TG_Connect( connectionId, 
            comPortName, 
            TG_BAUD_9600, 
            TG_STREAM_PACKETS );
    if( errCode < 0 ) {
        fprintf( stderr, "ERROR: TG_Connect() returned %d.\n", errCode );
        wait();
        exit( EXIT_FAILURE );
    }
    if( 0==TG_EnableBlinkDetection(connectionId,1)) //启动眨眼检测
    {
        printf("Success enable blink\n");
    }
    /* 不停的读取数据 */
    packetsRead = 0;
    while(1) 
    {
        /* 读一个报文 */
        errCode = TG_ReadPackets( connectionId, 1 );
        /* 如果这个报文读取成功 */
        if( errCode == 1 )
        {
            int att, det, sig;
            if(( errCode = TG_GetValueStatus(connectionId, TG_DATA_ATTENTION)) != 0 ) 
            {
                att = TG_GetValue(connectionId, TG_DATA_ATTENTION) ;
                det = TG_GetValue(connectionId, TG_DATA_MEDITATION);
                sig = TG_GetValue(connectionId, TG_DATA_POOR_SIGNAL);
                printf("attentin = %d, meditation=%d, signal=%d\n", att, det, sig);
            }
        } 
        else
        {
            printf("ReadPackets:errcode=%d\n", errCode);
        }
    } 
     //关闭连接
    TG_FreeConnection( connectionId );
    wait();
    return( EXIT_SUCCESS );
}
