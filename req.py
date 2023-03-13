# from queue import Queue
# from time import sleep
#
# from bs4 import BeautifulSoup as bs
# from requests import Session
# from aiohttp import ClientSession
#
# # with Session() as session:
# #     response = session.get(
# #         url='https://catalog.onliner.by/sdapi/catalog.api/search/mobile',
# #         params={
# #             'mobile_type[0]': 'smartphone',
# #             'mobile_type[operation]': 'union',
# #             'group': 1
# #         }
# #     )
# #     print(response.json())
# #     print(response.status_code)
#
#
# # with Session() as session:
# #     response = session.get(url='https://sputnik.by/economy/')
# # soup = bs(response.text, 'lxml')
# # divs = soup.find_all('div', class_='list__item')
# # for div in divs:
# #     title = div.find('a', class_='list__title')
# #     print(title.text)
# #     print(title['href'])
#
# # with Session() as session:
# #     response = session.get(
# #         url='https://api.belpost.by/api/v1/ops'
# #     )
# #     print(response.status_code)
# #     if response.status_code == 200:
# #         for i in range(response.json().get('last_page') - 1):
# #             response = session.get(url=response.json().get('next_page_url'))
# #             print(response.url)
# # import asyncio
#
#
# # async def get_response(page: int):
# #     async with ClientSession(base_url='https://api.belpost.by') as session:
# #         async with session.get(url='/api/v1/ops', params={'page': page}) as response:
# #             print(response.status)
# #             # print(await response.text())
# #             # print(await response.json())
# #
# #
# # async def main():
# #     tasks = [asyncio.create_task(get_response(i)) for i in range(1, 237)]
# #     for task in tasks:
# #         await task
# #
# # if __name__ == '__main__':
# #     asyncio.run(main())
#
#
# # def get_response(page):
# #     with Session() as session:
# #         response = session.get(
# #             url='https://api.belpost.by/api/v1/ops',
# #             params={'page': page}
# #         )
# #         print(response.status_code)
# #
# #
# # if __name__ == '__main__':
# #     from multiprocessing import Process
# #     threads = [Process(target=get_response, args=(page, )) for page in range(1, 201)]
# #     for thread in threads:
# #         thread.start()
#
# # from threading import Thread, Timer, current_thread, Lock, Semaphore, Barrier
# #
# # lock1 = Lock()
# # s = Semaphore(5)
# # q = Queue()
# #
# #
# # def main(j=None):
# #     if j:
# #         for i in range(10):
# #             q.put(i)
# #     else:
# #         obj = q.get()
# #         print(obj)
# #
# # #
# # threads = [Thread(target=main, name=f'Thread-{i}', args=(True,) if i == 0 else ()) for i in range(10)]
# # for thread in threads:
# #     thread.start()
#
# from asyncio import Queue, LifoQueue, Semaphore, Lock
# import asyncio
#
# q = Queue()
# s = Semaphore(5)
#
#
# async def task(i):
#     print(i)
#     await asyncio.sleep(2)
#
#
# async def run_tasks(i):
#     await s.acquire()
#     await task(i)
#     s.release()
#
#
# async def main():
#     tasks = [asyncio.create_task(run_tasks(i)) for i in range(10)]
#     for task in tasks:
#         await task
#
#
# asyncio.run(main())
