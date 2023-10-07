
import pygame,random

class Block :
	def __init__(self):
		self.count = 0
		self.time = 40
		self.next=random.randint(40,60)
		self.Blocks=[]
		self.add()
		
	def get_rects(self):
		return [d.get_rect() for d in self.Blocks ]
	def add(self):
		
		self.time+=1
		if self.time>self.next:
			tt=self.count//4
			if tt>20:
				tt=20
			self.next=random.randint(40-tt,50-tt)
			self.time=0
			color=random.choice([(120,120,200),(120,200,120),(200,120,120),(50,50,150),(150,50,50),(50,150,50)])
			self.count+=1
			h=random.randint(100,300)
			h2=600-150-h
			ss=-6-(self.count/10)
		
			
			box=Box((800,10),(40,h),speed=(ss,0),color=color)
			
			self.Blocks.append(box)
			
			box=Box((800,600-h2),(40,h2),speed= (ss ,0),color=color)
			
			self.Blocks.append(box)
			self.count+=1
			
	def draw(self,screen):
		self.add()
		for b in self.Blocks:
			b.draw(screen)
		for b in self.Blocks:
			
			rec=b.get_rect()
			if rec.x<(-1*rec.width):
				self.Blocks.remove(b)
				break
			elif rec.x>screen.get_rect().width:
				b.move()
				
			
			
		
		
class Box :
	def __init__(self,pos,dym,color=0,speed=(0,0),strok=0,g=0):
		self.g=g
		self.pos=pos
		self.speed=speed
		if color==0:
			self.color=(100,200,155)
		else:
			self.color=color
		self.dym=dym
		self.strok=strok
		
	def gravity(self,g):
		if self.speed[1]<20:
			self.speed=(self.speed[0],self.speed[1] + g)
		
	def jump(self,h=15):
		self.speed=(self.speed[0] ,  - h)
		
	def move(self):
		self.pos=(self.pos[0]+self.speed[0],self.pos[1]+self.speed[1])
	def draw(self,screen):
		if self.g>0:
			self.gravity(self.g)
		self.move()
		pygame.draw.rect(screen,self.color,pygame.Rect(self.pos,self.dym),self.strok )
	def get_rect(self):
		return pygame.Rect(self.pos,self.dym )


pygame.init()
ticks=25
me=Box((200,0),(30,30),speed=(0,0),g=2)
screen = pygame.display.set_mode( (800,600) )

font = pygame.font.SysFont(None, 60)

clock = pygame.time.Clock()

start_time = pygame.time.get_ticks() 

counting_time = 0

x,y=0,0
    	
	

paused  = False
running = True 
game_over=False
score=0

blocks=Block()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        

        if event.type == pygame.MOUSEBUTTONDOWN :
            if game_over:
            	score=0
            	me=Box((200,50),(30,30),speed=(0,0),g=2)
            	blocks=Block()
            	game_over=False
            else:
            	me.jump(15)
        if event.type == pygame.KEYDOWN :
            me.jump(15)
            if event.key == pygame.K_ESCAPE:
                running = False 
 
            if event.key == pygame.K_SPACE:
                paused = not paused

    screen.fill( (10,10,15) )
    srect=pygame.Rect(5,5,790 ,590 )
    
   
    if not srect.colliderect( me.get_rect() ) or not me.get_rect().collidelist(blocks.get_rects())== -1 :
    	game_over=True
    	
    if game_over:
    	o_text = font.render(f"Game Over your scor is {score}", 60 , (255,25,5))
    	
    	o_rect = o_text.get_rect(center = srect.center)
    	screen.blit(o_text, o_rect)
    else:
    	
    	me.draw(screen)
    	
    	blocks.draw(screen)
    	
    	o_text = font.render(f"scor : {score}", 60 , (175,175,175))
    	
    	o_rect = o_text.get_rect(topleft = (srect.topleft[0]+15 , srect.topleft[1]+15 ))
    	screen.blit(o_text, o_rect)
    	score+=1
    	
    pygame.draw.rect(screen ,(180,255,130) , srect , 6 )
    
    pygame.display.update()

    clock.tick(ticks)