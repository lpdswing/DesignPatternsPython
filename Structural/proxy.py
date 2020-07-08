# 代理模式

# 虚拟代理
class LazyProperty:

    def __init__(self, method):
        self.method = method
        self.method_name = method.__name__

    def __get__(self, instance, owner):
        if not instance:
            return None
        value = self.method(instance)
        setattr(instance, self.method_name, value)
        return value


class Test:

    def __init__(self):
        self.x = 'foo'
        self.y = 'bar'
        self._resource = None

    # resource方法使用LazyProperty修饰
    @LazyProperty
    def resource(self):
        print(f'init resource: resource is {self._resource}')
        self._resource = tuple(range(5))
        return self._resource


# 保护代理
class NotFindError(Exception):
    def __init__(self, msg):
        self.msg = msg


class RealSubject:
    def __init__(self):
        self.score = {
            "张三": 90,
            "李四": 59,
            "王二": 61
        }

    def num_students(self):
        num = len(self.score.keys())
        print("The number of students is {num}".format(num=num))

    def get_score(self, user_name):
        _score = self.score.get(user_name)
        print("The score of {user} is {score}".format(user=user_name,
                                                      score=_score))


class Proxy(object):
    def __init__(self):
        self.default_passwd = "9l0skjlsa"
        self.real_subject = RealSubject()

    def num_students(self):
        self.real_subject.num_students()

    def get_score(self, user_name):
        print("You are visiting {} score ...".format(user_name))
        passwd = input("Please input password : ")
        if passwd == self.default_passwd:
            if user_name in self.real_subject.score.keys():
                return self.real_subject.get_score(user_name)
            else:
                raise NotFindError("The student you are visiting not found.")
        else:
            raise ValueError("The password you provided is wrong!")


def client():
    proxy = Proxy()
    proxy.get_score("张三")


if __name__ == '__main__':
    t = Test()
    print(t.x)
    print(t.y)
    print(t.resource)
    print(t.resource)
    # 初始化字符串只执行了一次

    client()
