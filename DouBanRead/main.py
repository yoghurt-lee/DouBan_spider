#coding:utf-8
import os
import time

from DouBanRead import start_spider, print_into_excel
from DouBanRead import path


if __name__=="__main__":
    if not os.path.exists(path):
        os.makedirs(path)
    book_tag_lists = ['东野圭吾']
    start_time = time.time()
    book_lists = start_spider(book_tag_lists)
    print_into_excel(book_tag_lists,book_lists)#write into excel
    end_time = time.time()
    print "Done, the operation took %.3f seconds" % (end_time-start_time)