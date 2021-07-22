# Домашнее задание к занятию «Программирование на Go - структуры и методы»

В качестве результата пришлите ответы на вопросы в личном кабинете студента на сайте [netology.ru](https://netology.ru).

**Важно**: GoLand устанавливать не обязательно (но очень желательно), вы можете набирать текст программ в любом текстовом редакторе и запускать из консоли командой: `go run main.go`, либо собирать с помощью команды: `go build -o main main.go`.

## Задача "Windows"

**Важно**: данную ДЗ нужно выполнять в ОС Windows

### Легенда

На основании проекта с лекции (см. листинг файла под катом) реализовать сборку списка пользователей в ОС Windows.

<details>
<summary>Файл с лекции</summary>

```go
package main

import (
	"encoding/json"
	"log"
	"os"
	"os/exec"
	"os/user"
)

func main() {
	current, err := user.Current()
	// err + Tab напишет за вас
	if err != nil {
		log.Print(err)
		// завершает работу с ненулевым кодом возврата
		os.Exit(1)
		// т.е. следующая строка исполнена не будет
	}

	// выполняем только если не зашли в if
	data, err := json.Marshal(current)
	if err != nil {
		log.Print(err)
		os.Exit(1)
	}
	log.Print(data)         // распечатаются "байты"
	log.Print(string(data)) // преобразовываем слайс байт в строку

	command := "cat /etc/passwd"
	sh := "sh"
	c := "-c"
	
	// TODO: пишите код здесь
	
	cmd := exec.Command(sh, c, command)
	output, err := cmd.Output() // запускает команду и возвращает вывод в виде []byte
	if err != nil {
		log.Print(err)
		os.Exit(1)
	}
	log.Print(string(output))
}
```
</details>

### Выполнение

1. Посмотрите на пакет [runtime](https://golang.org/pkg/runtime/), а именно на переменную `GOOS` (использовать как `runtime.GOOS`), в которой могут храниться значения `windows`, `linux`, `darwin` (и другие - см. вывод команды `go tool dist list` значение до `/`, например, `linux/386`, `linux` - `GOOS`, `386` - `GOARCH`, целевая архитектура)
1. Если значение вышеуказанной переменной равно `windows`, то замените `command` на команду для вывода списка пользователей в ОС Windows, `sh` на `cmd`, а `c` на `/C` (см. подсказки)
1. Согласно приложенному ниже описанию сформируйте сборочные (`bat` или `sh`) скрипты для сборки под разные ОС
1. Запустите приложение под Windows и убедитесь, что вы получаете нужный список пользователей
1. Проведите исследование и ответьте на следующий вопросы:
   1. За что отвечает флаг `-c` в `sh` и `/C` в `cmd`? 
   1. Что будет, если попробовать исполнить те же команды напрямую в вашем приложении, без `sh -c` или `cmd /C`?
   
<details>
<summary>Подсказка по команде для вывода пользователей</summary>

Обратите внимание на команду `net` (см. `net /?`).
</details>

<details>
<summary>Подсказка по программной реализации</summary>

```go
package main

import (
	"encoding/json"
	"log"
	"os"
	"os/exec"
	"os/user"
	"runtime"
)

func main() {
	current, err := user.Current()
	// err + Tab напишет за вас
	if err != nil {
		log.Print(err)
		// завершает работу с ненулевым кодом возврата
		os.Exit(1)
		// т.е. следующая строка исполнена не будет
	}

	// выполняем только если не зашли в if
	data, err := json.Marshal(current)
	if err != nil {
		log.Print(err)
		os.Exit(1)
	}
	log.Print(data)         // распечатаются "байты"
	log.Print(string(data)) // преобразовываем слайс байт в строку

	log.Print(runtime.GOOS)


	command := "cat /etc/passwd"
	sh := "sh"
	c := "-c"
	if runtime.GOOS == "windows" {
		command = "??? ваша команда здесь ???"
		sh = "cmd"
		c = "/C"
	}
	cmd := exec.Command(sh, c, command)
	output, err := cmd.Output() // запускает команду и возвращает вывод в виде []byte
	if err != nil {
		log.Print(err)
		os.Exit(1)
	}
	log.Print(string(output))
}
```
</details>

<details>
<summary>Подсказка по -c, /C</summary>

Попробуйте сравнить вывод (версия для Linux):
```go
cmd := exec.Command("sh", "-c", "echo $PATH")
```

```go
cmd := exec.Command("echo", "$PATH")
```

Вернитесь к лекции по Си и попробуйте сравнить с поведением вот этой программы:
```c
#include <stdlib.h>

int main() {
    system("echo $PATH"); // echo PATH в Windows
    return 0;
}
```

Возможно, вам поможет раздел `Overview` из документации на пакет `exec`:
```
Package exec runs external commands. It wraps os.StartProcess to make it easier to remap stdin and stdout, connect I/O with pipes, and do other adjustments.

Unlike the "system" library call from C and other languages, the os/exec package intentionally does not invoke the system shell and does not expand any glob patterns or handle other expansions, pipelines, or redirections typically done by shells. The package behaves more like C's "exec" family of functions. To expand glob patterns, either call the shell directly, taking care to escape any dangerous input, or use the path/filepath package's Glob function. To expand environment variables, use package os's ExpandEnv.
```

Доп.ссылки для изучения:
* [`system` в Windows](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/system-wsystem?view=msvc-160)
* [`system` в man](https://man7.org/linux/man-pages/man3/system.3.html)

</details>

#### Написание сборочного скрипта

Для того, чтобы скомпилировать исполняемый файл под конкретную архитектуру, необходимо сделать следующее:
1. Установить переменную окружения `GOOS` в целевое значение, например, `windows`
1. Установить переменную окружения `GOARCH` в целевое значение, например, `amd64`
1. Установить переменную окружения `CGO_ENABLED` в значение `0`
1. Выполнить команду `go build -o main.exe main.go`

Используя ваши знания по написанию сценариев командной оболочки, реализуйте скрипты `bat` или `sh`, автоматизирующие данные операции.

<details>
<summary>Подсказка по сборочному скрипту (bat)</summary>

```bat
@ECHO OFF

:: устанавливаем целевую архитектуру
SET GOARCH=amd64
:: отключаем зависимость от libc
SET CGO_ENABLED=0

:: устанавливаем целевую ОС и собираем
SET GOOS=windows
go build -o client.exe main.go

:: устанавливаем целевую ОС и собираем
SET GOOS=linux
go build -o client.bin main.go

:: устанавливаем целевую ОС и собираем
SET GOOS=darwin
go build -o client.ibin main.go
```
</details>

<details>
<summary>Подсказка по сборочному скрипту (sh)</summary>

```sh
#!/bin/sh

# в nix достаточно перед командой выставить переменные в формате key=value
GOARCH=amd64 CGO_ENABLED=0 GOOS=windows go build -o client.exe main.go

GOARCH=amd64 CGO_ENABLED=0 GOOS=linux go build -o client.bin main.go

GOARCH=amd64 CGO_ENABLED=0 GOOS=darwin go build -o client.ibin main.go
```
</details>

### Результаты

В качестве результата пришлите:
1. Исходный код вашего приложения
1. Ответ на вопрос по поводу `sh -c` и `cmd /C`
1. Сборочный скрипт (перед отправкой переименуйте его в `build.bat.txt` или `build.sh.txt` соответственно - система загрузки Netology не разрешает загружать `sh` и `bat`)
1. Пример вывода вашей программы в ОС Windows (нужно запустить приложение и сделать скриншот вывода - если вы делаете на своей основной машине, то не забудьте с помощью Paint или любого иного инструмента "замазать" реальные данные)

В качестве результата пришлите указанные выше пункты в личном кабинете студента на сайте [netology.ru](https://netology.ru).
