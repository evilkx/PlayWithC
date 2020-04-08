#include <graphics.h>
#include <conio.h>
#include <time.h>
#include <iostream>

constexpr auto VI_FUNC_NUM = 6;		//定义视觉刺激的个数;

struct VI_FUNC
{
	int		width;
	int		height;
	double	freq;
	int		color;
};

VI_FUNC vifucs[VI_FUNC_NUM];

// Draw_BlinkRec(int x, int y)

void Draw_BlinkRec_16hz(int x, int y, int f) {
	double t;
	t = (1.0 / f) * 1000;
	RECT r = { x, y-20, x+200, y };
	setcolor(BLACK);
	drawtext(_T("16Hz"), &r, DT_SINGLELINE | DT_CENTER);
	solidrectangle(x, y, x+200, y+200);
	Sleep(t);
	clearrectangle(x, y, x+200, y+200);
	Sleep(t);
	//std::cout << t <<"\n";
}

void draw_blink_rec() {
	RECT r = { 500, 80, 700, 100 };
	setcolor(BLACK);
	drawtext(_T("10Hz"), &r, DT_SINGLELINE | DT_CENTER);
	solidrectangle(500, 100, 700, 300);
	Sleep(50);
	clearrectangle(500, 100, 700, 300);
	Sleep(50);
}

int main(void) {
	initgraph(1280, 720);
	setbkcolor(LIGHTGRAY);
	cleardevice();
	//setlinecolor(BLACK);
	//solidrectangle(200, 100, 400, 300);
	//rectangle(500, 100, 700, 300);
	//fillrectangle(800, 100, 1000, 300);
	//clearrectangle(800, 100, 1000, 300);

	MOUSEMSG m;		// 定义鼠标消息
	while (!_kbhit())
	{
		Draw_BlinkRec_16hz(400, 100, 16);
		rectangle(200, 500, 300, 550);
		RECT r1 = { 200, 500, 300, 550 };
		setcolor(BLACK);
		drawtext(_T("10Hz"), &r1, DT_SINGLELINE | DT_CENTER);
		rectangle(350, 500, 450, 550);
		RECT r2 = { 350, 500, 450, 550 };
		setcolor(BLACK);
		drawtext(_T("12Hz"), &r2, DT_SINGLELINE | DT_CENTER);
		rectangle(500, 500, 600, 550);
		RECT r3 = { 500, 500, 600, 550 };
		setcolor(BLACK);
		drawtext(_T("14Hz"), &r3, DT_SINGLELINE | DT_CENTER);
		rectangle(650, 500, 750, 550);
		RECT r4 = { 650, 500, 750, 550 };
		setcolor(BLACK);
		drawtext(_T("16Hz"), &r4, DT_SINGLELINE | DT_CENTER);
		line(1000, 0, 1000, 720);

		m = GetMouseMsg();

		switch (m.uMsg)
		{
			case MOUSEEVENTF_LEFTDOWN:
			/*
			if (m.x>=200&&m.x<=300&&m.y>=500&&m.y<=550)
			{
				std::cout << "hello!";
			}
			*/
				setcolor(BLACK);
				rectangle(m.x - 5, m.y - 5, m.x + 5, m.y + 5);
				break;
			default:
				break;
		}
	}
	_getch();
	closegraph();

	return 0;
}
