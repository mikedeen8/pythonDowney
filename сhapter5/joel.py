def joel():
    text = input('Джоел жив?\n')
    if text == 'Да' or  text =='да':
        joel()
    else:
        print('Да, он мёртв')

joel()