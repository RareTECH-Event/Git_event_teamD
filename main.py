def main():
    while True:
        print("選択してください：")
        print("1: しゅーぽ")
        print("2: ゆうすけ")
        print("3: ヨウズ")
        print("q: 終了")

        choice = input("> ")

        if choice == "1":
            print("こんばんは")
        elif choice == "2":
            print("初心者です")
        elif choice == "3":
            print("今日はみなさんありがとうございました")
        elif choice == "q":
            print("プログラムを終了します。")
            break
        else:
            print("無効な入力です。もう一度選択してください。")

if __name__ == "__main__":
    main()

