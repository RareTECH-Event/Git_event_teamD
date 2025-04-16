def main():
    while True:
        print("選択してください：")
        print("1: メンバー1の名前")
        print("2: ゆうすけ")
        print("3: ヨウズ")
        print("4: よぅずver.2.0")
        print("q: 終了")

        choice = input("> ")

        if choice == "1":
            print("メンバー1のコメント")
        elif choice == "2":
            print("初心者です")
        elif choice == "3":
            print("今日はみなさんありがとうございました")
        elif choice == "4":
            print("早起きは三文の得。でも、三文っていくら？")
        elif choice == "q":
            print("プログラムを終了します。")
            break
        else:
            print("無効な入力です。もう一度選択してください。")

if __name__ == "__main__":
    main()

