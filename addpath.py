#! /usr/bin/env python
# -*- coding: utf-8 -*-
# By i@BlahGeek.com at 09/21/2013

import sqlite3

def addPath(name, root, editable):
    conn = sqlite3.connect('main.db')
    try:
        c = conn.cursor()
        c.execute('insert into path values (?, ?, ?)', 
                    (name, root, editable))
    except sqlite3.OperationalError:
        c.execute('create table path (name varchar primary key, '
                  'root varchar, editable boolean)')
        raise
    finally:
        conn.commit()
        conn.close()

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 3:
        addPath(sys.argv[1], sys.argv[2], bool(int(sys.argv[3])))
    else:
        addPath(sys.argv[1], sys.argv[2], False)

