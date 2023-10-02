using System;
using System.Runtime.InteropServices;
using System.Threading;

class Program
{
    [DllImport("user32.dll")]
    private static extern IntPtr FindWindow(string? lpClassName, string lpWindowName);

    [DllImport("user32.dll")]
    private static extern bool SetForegroundWindow(IntPtr hWnd);

    [DllImport("user32.dll")]
    private static extern bool PostMessage(IntPtr hWnd, uint Msg, int wParam, int lParam);

    private const uint WM_KEYDOWN = 0x0100;
    private const uint WM_KEYUP = 0x0101;

    static void Main()
    {
        // Здесь ты должен указать заголовок окна, в котором хочешь выполнить действия.
        string windowTitle = "Evades - Opera";

        // Найти окно по заголовку.
        IntPtr? hWnd = FindWindow(null, windowTitle); // Изменено на IntPtr?

        // Если окно не найдено, то можно выйти или обработать эту ситуацию по-другому.
        if (hWnd == null || hWnd == IntPtr.Zero)
        {
            Console.WriteLine("Окно не найдено");
            return;
        }

        // Сделать окно активным.
        SetForegroundWindow(hWnd.Value);

        // Подождать некоторое время, чтобы окно обработало действие.
        //Thread.Sleep(1000);

        // Отправить клавишу D в окно.
        for(int i = 0; i < 5000; i++)
        {
            PostMessage(hWnd.Value, WM_KEYDOWN, (int)ConsoleKey.D, 0);
        }
            PostMessage(hWnd.Value, WM_KEYUP, (int)ConsoleKey.D, 0);
        // Подождать некоторое время, чтобы окно обработало действие.
        //Thread.Sleep(1000);

        // Теперь можно выполнить другие действия, если нужно.

        // Вернуть фокус на предыдущее активное окно (по желанию).
        //IntPtr previousForegroundWindow = FindWindow(null, null); // Получить окно по умолчанию (Desktop)
        //SetForegroundWindow(previousForegroundWindow);
    }
}
