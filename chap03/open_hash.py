from __future__ import annotations
from typing import Any, Type
from enum import Enum
import hashlib

class Status(Enum):
    OCCUPIED = 0 #저장되어 있는 상태
    EMPTY = 1 #비어 있음
    DELETED = 2 #삭제 완료

class Bucket:
    def __init__(self, key: Any = None, value: Any = None, stat: Status = Status.EMPTY)->None:
        #초기화
        self.key=key
        self.value=value
        self.stat=stat
    
    def set(self, key: Any, value: Any, stat: Status) -> None:
        #모든 필드에 값을 설정
        self.key=key
        self.value=value
        self.stat=stat

    def set_status(self, stat: Status) -> None:
        #속성 설정
        self.stat=stat
    
class OpenHash:
    #오픈주소 해시 클래스
    def __init__(self, capacity: int)->None:
        #초기화
        self.capacity=capacity
        self.table=[Bucket()]*self.capacity

    def hash_value(self, key: Any)->int:
        #해시값구하기
        if isinstance(key, int):
            return key %self.capacity
        return (int(hashlib.md5(str(key).encode()).hexdigest(),16)%self.capacity)

    def rehash_value(self, key: Any)->int:
        return (self.hash_value(key)+1)%self.capacity

    def search_node(self, key: Any)->Any:
        #키가 key인 버킷을 검색
        hash=self.hash_value(key)
        p=self.table[hash]

        for i in range(self.capacity):
            if p.stat==Status.EMPTY:#키 값이 없는 경우
                break
            elif p.stat==Status.OCCUPIED and p.key==key:#키를 찾음
                return p
            hash=self.rehash_value(hash)#키가 다른 곳에 저장되어 있는 경우
            p=self.table[hash]
        return None
    
    def search(self, key: Any)->Any:
        #키가 key인 원소를 검색하여 값을 반환
        p=self.search_node(key)
        if p is not None:
            return p.value
        else:
            return None

    def add(self, key: Any, value: Any)->bool:
        #키가 key이고 값이 value인 원소를 추가
        if self.search(key) is not None:
            return False #이미 등록된 키
        
        hash = self.hash_value(key)
        p=self.table[hash]
        for i in range(self.capacity):
            if p.stat==Status.EMPTY or p.stat == Status.DELETED:#비었거나 이미 삭제된 경우
                self.table[hash]=Bucket(key, value, Status.OCCUPIED)#버킷에 저장하고 저장된 상태로 기록
                return True
            hash =self.rehash_value(hash)#재해시
            p=self.table[hash]
        return False #해시테이블이 가득 참

    def remove(self, key: Any)->int:
        p=self.search_node(key)
        if p is None:
            return False
        p.set_status(Status.DELETED)#삭제된 것으로 기록
        return True

    def dump(self)->None:
        for i in range(self.capacity):
            print(f'{i:2} ', end='')
            if self.table[i].stat==Status.OCCUPIED:#저장된 상태
                print(f'{self.table[i].key} ({self.table[i].value})')
            elif self.table[i].stat==Status.EMPTY:#비워진 상태
                print('-- 미등록 --')
            elif self.table[i].stat==Status.DELETED:#삭제된 상태
                print('-- 삭제 완료 --')