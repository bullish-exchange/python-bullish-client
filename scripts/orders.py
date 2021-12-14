from bullish import Bullish
from bullish.objects.order import OrderCreate, OrderCancel
import time
import config

if __name__ == '__main__':

    conn = Bullish(config.hostname, 
                   config.api_key_priv, config.metadata, verify=False)
                   
    # login
    conn.login()
    
    nonce = conn.get_nonce()
    print(nonce.__dict__)

    for i in range(0, 10):
        new_ord = OrderCreate(
                          handle=f'{i}',
                          symbol='BTCUSD',
                          type='LMT',
                          side='BUY',
                          price='1000.0000',
                          stopPrice='',
                          quantity='2.00000000',    # requires 8 places after decimal for BTC
                          timeInForce='GTC'
                          )
        created_order = conn.create_order(new_ord)
        time.sleep(1)


    # page through orders
    is_paging = True
    all_orders = []
    next_page = ''
    while is_paging:
        print('get_orders: OPEN')
        if next_page:
            orders = conn.get_orders(_metadata=True, 
                                 symbol='BTCUSD', 
                                 status='OPEN', 
                                 _pageSize=5, 
                                 _nextPage=next_page)
        else:
            orders = conn.get_orders(_metadata=True, 
                                 symbol='BTCUSD', 
                                 status='OPEN', 
                                 _pageSize=5)
        if len(orders.data) > 0:
            print(f'Got {len(orders.data)} orders')
            all_orders += orders.data
        else:
            print("No OPEN orders")
        if not orders.links.next:
            is_paging = False
        else:
            next_page = orders.links.next

    print(all_orders)
    for ord in all_orders:
        print(f'Cancelling {ord.orderId} {ord.handle} {ord.symbol}')
        cancel_ord_info = conn.get_order_by_id(ord.orderId)
        cancel_ord = OrderCancel(orderId=cancel_ord_info.orderId, symbol=cancel_ord_info.symbol)
        cancelled = conn.cancel_order(cancel_ord)
        time.sleep(1)