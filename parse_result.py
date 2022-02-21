def main():
    with open(".tmp_test_ia_rec.pg", 'r') as fd:
        blanc = 0
        noir  = 0
        # Parcours des lignes
        for line in fd:
            words = line.split(" ")
            # Parcours des mots
            for word in words:
                if word == "BLANC":
                    blanc += 1
                elif word == "NOIR":
                    noir +=1
        print("Noir:", noir, "Blanc:", blanc)


if __name__ == '__main__':
    main()
