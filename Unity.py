class Object:
    def __init__(self, name, hp, physical_pow):
        self.name = name
        self.hp = hp
        self.physical_pow = physical_pow
        print(f'{self.name} 이(가) 생성 되었습니다.')
        print(f'체력 : {self.hp}, 물리 공격력 : {self.physical_pow}')
    
    def attack(self, target):
        print(f'{self.name}가 {target.name}을 {self.physical_pow}의 물리 공격력으로 공격했습니다.')
        target.hp -= self.physical_pow 
        return target.hp # 리턴은 재할당 해줌.

    def status(self):
        if self.hp > 0:
          print(f'{self.name}의 체력 : {self.hp}')


class Player(Object):
    def __init__(self,  name, hp, physical_pow, magic_pow=50):
        Object.__init__(self, name, hp, physical_pow)
        self.magic_pow = magic_pow

    def magic_attack(self, target):
        print(f'{self.name}가 {target.name}을 {self.magic_pow}의 마법 공격력으로 공격했습니다.')
        target.hp -= self.magic_pow
        return target.hp
    
    def status(self):
        if self.hp > 0:
          print(f'{self.name}의 체력 : {self.hp}')


class Player(Object):
    def __init__(self,  name, hp, physical_pow, magic_pow=50):
        Object.__init__(self, name, hp, physical_pow)
        self.magic_pow = magic_pow

    def magic_attack(self, target):
        print(f'{self.name}가 {target.name}을 {self.magic_pow}의 마법으로 공격했습니다.')
        target.hp -= self.magic_pow
        return target.hp


class Monster(Object):
    def cure(self):
        
        self.hp += 10
        print(f'{self.name}가 자신의 체력을 10만큼 회복했습니다. 현재 체력 : {self.hp}')
        return self.hp

    def wait(self):  
        print(f'{self.name}가 대기했습니다.')



def player_action():
    print('---- 공격 스킬 선택 ------')
    print('------1. 물리 공격---------')
    print('-------2. 마법 공격--------')
    p1_skill_input = int(input('사용할 스킬의 번호를 입력하세요. : '))

    print('-------대상 선택 phase --------')
    print('---1.고블린---')
    print('---2.오크---')
    print('---3.빅보스 Waaah---')
    p1_target_input = int(input('공격할 대상의 번호를 입력하세요. : '))
    
    p1 = Player('워리어' , 100 , 10)
    m1 = Monster('고블린', 10, 10)
    m2 = Monster('오크', 30, 30)
    m3 = Monster('빅보스 Waaah', 30, 50)
        
    mon_list = [m1, m2, m3]
        
        
    if p1_skill_input == 1:  #공격 대상은 고블린
            
        if p1_target_input == 1:
            m1.hp = p1.magic_attack(m1) 
            
        elif p1_target_input == 2:
            m2.hp = p1.magic_attack(m2)  # 공격 대상은 오크
            
        elif p1_target_input == 3: #공격 대상은 빅보스
             m3.hp = p1.magic_attack(m3)
             
             
    def monster_action():

        if m1 in mon_list:
            # 고블린 행동
            action_num = reversed.randint(1, 3) # 행동 번호 결정
            if action_num == 1: # 자신 치유
                m1.cure()
            elif action_num == 2: # 대기
                m1.wait()
            elif action_num == 3: # 플레이어 공격
                p1.hp = m1.attack(p1)
        if m2 in mon_list:
            # 오크 행동
            action_num = reversed.randint(1, 3)
            if action_num == 1:
                m2.cure()
            elif action_num == 2:
                m2.wait()
            elif action_num == 3:
                p1.hp = m2.attack(p1)
        if m3 in mon_list:
            # 빅보스 Waaah 행동
            action_num = reversed.randint(1, 3)
            if action_num == 1:
                m3.cure()
            elif action_num == 2:
                m3.wait()
            elif action_num == 3:
                p1.hp = m3.attack(p1)
                
                
             
             
                              
        def monster_death():
            if m1.hp <= 0:
                if m1 in mon_list:
                    mon_list.remove(m1)
            if m2.hp <= 0:
                if m2 in mon_list:
                    mon_list.remove(m2)
            if m3.hp <= 0:
                if m3 in mon_list:
                    mon_list.remove(m3)  
                    
                    turn = 0
                    
                    while True:
                        
                        print('-----------------------턴 시작전 상태표시---------------------------------')  


                        p1.status()
                        
                        for m in mon_list:
                            m.status()
                            
                            
                        if turn % 2 == 0:
                            print('------플레이어 턴------') 
                            
                            
                            player_action()
                            
                            
                            monster_action()
                            
                            monster_death()
                            
                            if len(mon_list) <= 0:
                                print('모든 몬스터를 물리쳤습니다.')
                                print('----WIN!----') 
                                break
                            
                            
                            else:
                                print('---------MONSTER TURN-----------')
                                
                                
                                monster_action()
                                
                                if p1.hp <= 0:
                                    print('-----------플레이어 사망-------------')
                                    print('-----------Game Over-------------')
                                    break
                                
                                turn += 1
                                print('--------------------------------')
                                print('---------------Game Over-----------------')
                                break
                            
                        turn += 1
                        print('--------------------------------')
                        print('--------------- 턴 종료-----------------')
                        print('--------------------------------')
                            
                
                            

                                     










             
             
             
             
             
             
             
             
             
             
             
             
        