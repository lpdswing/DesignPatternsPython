# Python设计模式

> 代码参考自Python设计模式一书

## Part1.创建型模式
```text
工厂方法和抽象工厂设计模式都可以用于以下几种场景:
a.想要追踪对象的创建
b.想要将对象的创建和使用解耦
c.想要优化应用的性能和资源占用
```
### 工厂方法
在工厂方法模式中,我们执行单个函数,传入一个参数(提供信息表明我们想要什么),但并不要求知道任何关于对象如何实现以及对象来着哪里的细节.
- 生活中的例子

制作塑料玩具的材料是一样的,但是不同的模具就行生成出不同的外形.比如有个工厂方法,输入是目标外形(小汽车或变形金刚)的名称,输出则是塑料外形.

- 软件中的例子

Django框架使用工厂方法模式来创建表单字段.Django的forms模块支持不同类字段(CharField,EmailField
)的创建和定制(max_length,required).

### 抽象工厂
抽象工厂设计模式是抽象方法的一种泛化,一个抽象工厂是逻辑上的一组工厂方法,其中每个工厂方法负责生产不同种类的对象.

- 生活中的例子

汽车制造行业使用了抽象工厂的思想,冲压不同的汽车模型的部件使用的机件是相同的,机件装配起来的模型随时可配置,且易于改变.

- 软件中的例子

django_factory是一个用于在测试中创建Django
模型的抽象工厂实现,可以用来为支持测试专有属性的模型创建实例.让测试代码的可读性更高,且避免共享不必要的代码.

- 应用

抽象工厂方法是工厂方法的泛化,所以它能提供相同的好处,让对象的创建更容易追踪,将对象创建与使用解耦,提供优化内存占用和应用性能的潜力.
何时使用工厂方法,何时用抽象工厂方法? 通常一开始使用工厂方法,因为它更简单,如果后来发现应用需要许多工厂方法,那么将创建一系列对象的过程合并在一起更合理,从而使用抽象工厂.

### 建造者模式

- 生活中的例子

快餐店中,即使存在多种汉堡和不同包装,准备一个汉堡和打包的流程是相同的,经典汉堡和麻辣汉堡的区别在于表现,而不是建造过程,指挥者是出纳员,将需要准备什么餐品的指令传递给工作人员,
建造者是工作人员中的个体,关注具体的顺序.

- 软件中的例子

django-widgy,django-query-builder

- 使用

建造者模式可以在工厂模式不适用的场景中使用,以下几种情况下,建造者是更好的选择:
想要创建一个复杂对象,对象由多个部分构成,并且对象创建经历多个不同的步骤,这些步骤也许还需遵从特定的顺序,
要求一个对象有不同的表现,并希望将对象的构造与表现解耦.
想要在某个时间点创建对象,但在稍后的时间点访问.

### 原型模式

原型模式帮助我们创建对象的克隆,最简单的形式就是一个clone函数,接收一个对象作为参数,返回输入对象的一个副本.

- 生活中的例子

有丝分裂,细胞分裂的过程是生物克隆的一个例子,在这个过程中,细胞核分列成2个细胞核,每个都有和原来细胞相同的染色体和DNA.

- 软件中的例子

很多Python应用都使用了原型模式,但几乎都不称之为原型模式,因为对象克隆是编程语言的一个内置特性.deepcopy.


## Part2.结构型模式

### 适配器模式

用来实现2个不兼容接口之间的兼容,我们可以编写一层代码用于进行新旧接口的通信,这个代码层就叫适配器.

- 生活中的例子

在没有网口的笔记本上插网线就需要一个适配器.

- 软件中的例子

Grok框架,Python第三方包Traits也用了适配器模式.

- 使用

在某个产品制造出来,需要对应新的需求时,如果希望它仍然有效,使用适配器是个不错的方式,不要求访问他方源码,不违法开闭原则

### 修饰器模式

无论何时我们想对一个对象添加额外的功能,都有下面这些方法可选,如果合理,可以直接将功能添加到对象所属类,
使用组合,使用继承.与继承相比,通常应该先用组合,因为继承使代码更难复用,继承使静态的.

- 生活中例子
给枪加个消音器,使用不同的镜头照相.

- 软件中的例子
Django框架大量使用了修饰器,比如限制某些http请求对视图的访问.

- 使用
以下为横切关注点的一些例子: 数据校验,事务处理(数据库事务),缓存,日志,监控,调试,业务规则,压缩,加密.

### 外观模式
外观模式在随着系统变的非常复杂,最终形成大量的令人迷惑的交互,我们不想把这种复杂性暴露给客户端,外观模式可以
隐藏系统的内部复杂性,通过一个简单的接口向客户端暴露必要的部分,本质上外观模式是复杂系统实现的一个抽象层.

- 生活中的例子

当你致电银行或公司,通常会被连线到客服部门,客服在你和业务部门之间充当一个外观角色.

- 软件中的例子
django-oscar-datacash是一个第三方组件,用于继承DataCash支付网关.

### 享元模式
由于对象创建的开销,面相对象系统可能会面临性能问题,性能问题通常在资源受限的嵌入式系统出现,作为软件工程师,我们应该
编写更好的软件来解决问题,而不是要求客户买更好的硬件,享元模式通过为相似对象引入数据共享来最小化内存使用,提升性能.
一个享元就是一个包含状态的共享对象.

- 生活中的例子

不太容易找,我们可以把享元看做现实生活中的缓存区.比如许多书店都有专用的书架摆放最新的最流行的出版物.

- 软件中的例子

Peppy,它使用享元模式存储major mode状态栏的状态.

- 使用

应用需要使用大量的对象,对象太多,存储渲染的代价太大,对象id对于应用不重要.以上的场景享元是有效的.

### 控制器模式
关注点分离原则(SoC)的思想是将应用切分成不同的部分,为实现模型与其表现之间的解耦,每个视图通常需要一个属于它的控制器.

- 现实生活中的例子

MVC应用于面相对象编程的SOC原则,比如建房子通常会请不同的专业人员完成以下工作,安装管道和电路,粉刷房子.

- 软件中的例子

web2py框架,Django,Flask等

### 代理模式

在某些应用中,我们想在访问某个对象前执行一个或多个重要操作,例如访问敏感信息,我们希望用户具备足够的权限,
另一个案例,我们想把一个计算成本较高的对象创建过程延迟到用户真正使用它时进行. 这类操作通常使用代理设计模式.
```text
远程代理: 实际存在于不同地址空间的对象在本地的代理者.
虚拟代理: 用于懒初始化,将一个大计算量对象的创建延迟到真正需要的时候进行.
保护/防护代理: 控制对敏感对象的访问.
智能引用: 在对象呗访问时执行额外动作,此类代理例子包括引用计数和线程安全检查.

````
- 生活中例子

支票代理了银行账户

- 软件中例子

weakref模块包含一个proxy方法,该方法接收一个输入对象并将一个只能代理返给该对象.

### 桥接模式

在软件系统中,某些类型由于自身逻辑,具有2个或多个维度的变化,利用面相对象的技术使得该类型能够轻松的沿着多个方向
进行变化,而不引入额外的复杂度,就用桥接模式,将抽象部分与实现部分分离,使他们都可以独立的变化.

### 组合模式

组合模式（Composite Pattern），又叫部分整体模式，是用于把一组相似的对象当作一个单一的对象。组合模式依据树形结构来组合对象，用来表示部分以及整体层次。这种类型的设计模式属于结构型模式，它创建了对象组的树形结构。
这种模式创建了一个包含自己对象组的类。该类提供了修改相同对象组的方式。

## Part3.行为型模式

### 责任链模式

责任链模式用于让多个对象来处理单个请求时,或用于预先不知道应该由哪个对象来处理某个特殊请求时,原则如下:
1.存在一个对象链,链表,树或任何便捷的数据结构2.一开始将请求发送给链中的第一个对象.3对象决定是否处理该请求.
4.对象将请求转发给下一个请求.5.重复该过程,直到链尾.

- 生活中例子

atm机, 娃娃贩卖机等

- 软件中的例子

drf应该是,个人理解