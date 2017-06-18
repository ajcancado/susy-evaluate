#!/usr/bin/env python3

import subprocess
import sys
import os.path
import csv

from abc import ABC, abstractmethod

ErrorId = {}

class Evaluator(ABC):
    def init(self):
        pass

    @abstractmethod
    def execute(self, infile):
        pass

    @abstractmethod
    def process(self, result):
        pass

    def evaluate(self, files):
        self.init()

        for f in files:
            output = self.process(self.execute(f))
            if len(output) > 1:
                print(output)
            else:
                filename = f.split('/')[-1]
                message = '[{file}]: Nenhum erro de análise estática foi encontrado'
                print(message.format(file=filename))


class Cppcheck(Evaluator):

    def init(self):
        # TODO: Aqui será lido o arquivo CSV para preencher o dict
        with open('../csv/errorid.csv') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                ErrorId[reader.line_num] = row

    def execute(self, infile):
        process = subprocess.Popen(['cppcheck', '--enable=style',
                '--template={file}::{line}::{id}::{severity}::{message}',
                infile], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        retcode = process.wait()
        r = process.stdout.read()
        return r

    def process(self, result):
        result = result.strip().split(b'\n')
        result = result[1:]
        fmt_result = []
        for r in result:
            try:
                r = r.decode('utf-8')
                fname, fline, eid, sev, msg = r.split('::')
                filename = fname.split('/')[-1]
                if eid in self.ErrorId:
                    fmt_result.append(self.ErrorId[eid].format(file=filename,
                            line=fline, id=eid, severity=sev, message=msg))
            except:
                continue
        return '\n'.join(fmt_result)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(-1)

    ccheck = Cppcheck()
    with open(sys.argv[1]) as infile:
        file_list_temp = infile.read().strip().split('\n')
        file_list = []
        
        for f in file_list_temp:
            if os.path.exists(f):
                t = f.split('/')[-1].split('.')[-1]
                if t in ["c","cpp"]:
                    file_list.append(f)
        ccheck.evaluate(file_list)
