#写入文件
def write_cards(cards, filename):
    with open(filename, 'w', encoding='gbk') as fp:
        for card in cards:
            fp.write('{name},{tel},{company},{job},{addr}\n'.format(**card))

#读取文件
def read_cards(filename):
    """
       读取 文件中的名片信息, 合成名片盒子
       :param filename: csv文件路径
       :return:
       """

    with open(filename,'r',encoding='gbk') as fp:
        datas = fp.readlines()


    #定义一个名片盒子
    cards = []
    for data in datas:
        #去空格   获取列表
        value = data.strip().split(',')

        card = {
            'name':value[0],
            "tel": value[1],
            "company":value[2],
            "job":value[3],
            "addr":value[4]
            }

        # 添加到名片盒子
        cards.append(card)

    return cards

cards= read_cards('./名片管理系统')

#欢迎使用名片管理系统标题
def tsxx():
    print(
        """
        欢迎 使用源码时代定制名片管理系统
        *******************************
        功能列表:
        1. 添加名片
        2. 显示所有名片
        3. 修改名片
        4. 删除名片
        5. 查找名片

        0. 退出系统
        """
    )

#添加名片
def add_card():
    print("添加名片:")
    # 1. 添加名片: 根据用户录入的信息, 组装成字典 追加到名片盒子里面
    # 录入名片信息
    name = input("姓名:")
    tel = input("电话:")
    company = input("公司:")
    job = input("职位:")
    addr = input("地址:")
    # 组装成字典
    card = {"name": name, "tel": tel, "company": company, "job": job, "addr": addr}
    # 将名片追加到名片盒子里面
    cards.append(card)
    # 友情提示
    print(f"添加: {name} 名片成功!")

#显示所有名片
def all_card():
    print("显示所有名片:")
    # 2. 显示所有名片: 遍历名片盒子输出名片信息
    # 显示表头
    print("姓名\t|\t电话\t\t|\t公司\t\t|\t职位\t|\t地址")
    # 显示数据
    for card in cards:
        print(f"{card['name']}\t|\t{card['tel']}\t|\t{card['company']}\t|\t{card['job']}\t|\t{card['addr']}")

#修改名片
def update_card():
    print("修改名片:")
    # 3. 修改名片:  录入需要修改名片的姓名, 根据名字到名片合子查找对应的哪一张名片,
    #     如果找到 , 重写录入新的名片信息, 完成修改操作
    # 要求, 用户录入名片姓名, 遍历名片盒子一一比对名片中的姓名,如果比对成功说明找到,如果比对失败提示用户输入名字有误
    old_name = input("请录入需要修改名片姓名:")

    # 遍历名片盒子
    for card in cards:
        if card['name'] == old_name:
            # 如果找到 , 重写录入新的名片信息, 完成修改操作
            # 录入名片信息
            name = input("姓名:")
            tel = input("电话:")
            company = input("公司:")
            job = input("职位:")
            addr = input("地址:")

            # 组装成新的名片
            new_card = {"name": name, "tel": tel, "company": company, "job": job, "addr": addr}

            # 修改: 找到原来, 将其更新
            # 获取原来card名片的索引
            old_index = cards.index(card)
            # 修改对应索引的值
            cards[old_index] = new_card
            print(f"修改: {old_name} 的名片成功!!")
            break
    else:
        print(f"输入的名片姓名: {old_name} 不存在!!")

#删除名片
def del_card():
    print("删除名片:")
    # 删除名片: 录入需要删除名片的姓名, 根据名字到名片盒子中查到对应的名片并删除.
    old_name = input("请录入需要删除名片姓名:")

    # 遍历名片盒子
    for card in cards:
        if card['name'] == old_name:
            # 确定是否删除
            confirm = input("确定是否删除? [Y/N]")
            if confirm.lower() == "y":
                # 比对成功,删除名片
                cards.remove(card)
                # 友情提示
                print(f"删除 {old_name} 名片成功!")
            break
    else:
        print(f"输入的名片姓名: {old_name} 不存在!!")

#查找名片
def one_card():
    print("查找名片:")
    # 要求, 用户录入名片姓名, 遍历名片盒子一一比对名片中的姓名,如果比对成功说明找到,如果比对失败提示用户输入名字有误
    old_name = input("请录入名片姓名:")

    # 遍历名片盒子
    for card in cards:
        if card['name'] == old_name:
            # 比对成功,打印名片
            print(
                f"""
                           **************************************************
                           姓名: {card['name']}            电话:{card['tel']}
                           公司: {card['company']}         职位:{card['job']}
                           地址: {card['addr']}
                           **************************************************
                           """
            )
            break
    else:
        print(f"输入的名片姓名: {old_name} 不存在!!")

if __name__ == '__main__':
    while True:
        tsxx()
        num = input("请选择 功能序号:")
        if num == '1':
            add_card()
        if num == '2':
            all_card()
        if num=="3":
            update_card()
        if num=="4":
            del_card()
        if num=="5":
            one_card()
        if num=='0':
            quit('退出系统')


        write_cards(cards,'./名片管理系统')