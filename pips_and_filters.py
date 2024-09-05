import csv
from loguru import logger
import time

class Pipe:
    def __init__(self):
        self.data = []
    
    def set_data(self, data):
        self.data = data
    
    def get_data(self):
        return self.data

class CSVReaderFilter:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def process(self, pipe):
        logger.info(f"Lendo dados do arquivo CSV: {self.file_path}")
        start_time = time.time()
        with open(self.file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
            pipe.set_data(data)
        end_time = time.time()
        duration = end_time - start_time
        throughput = len(data) / duration if duration > 0 else float('inf')
        logger.info(f"{len(data)} registros lidos e armazenados no pipe. Tempo de leitura: {duration:.4f} segundos. Throughput: {throughput:.2f} registros/segundo.")

class AltaFilter:
    def process(self, pipe):
        data = pipe.get_data()
        logger.info(f"Aplicando filtro de alta. Registros antes do filtro: {len(data)}")
        start_time = time.time()
        filtered_data = [row for row in data if row['alta'] == 'Nao']
        pipe.set_data(filtered_data)
        end_time = time.time()
        duration = end_time - start_time
        throughput = len(filtered_data) / duration if duration > 0 else float('inf')
        logger.info(f"Registros após o filtro de alta: {len(filtered_data)}. Tempo de aplicação do filtro: {duration:.4f} segundos. Throughput: {throughput:.2f} registros/segundo.")

class AgeFilter:
    def __init__(self, min_age):
        self.min_age = min_age

    def process(self, pipe):
        data = pipe.get_data()
        logger.info(f"Aplicando filtro de idade. Idade mínima: {self.min_age}. Registros antes do filtro: {len(data)}")
        start_time = time.time()
        filtered_data = [row for row in data if int(row['idade']) > self.min_age]
        pipe.set_data(filtered_data)
        end_time = time.time()
        duration = end_time - start_time
        throughput = len(filtered_data) / duration if duration > 0 else float('inf')
        logger.info(f"Registros após o filtro de idade: {len(filtered_data)}. Tempo de aplicação do filtro: {duration:.4f} segundos. Throughput: {throughput:.2f} registros/segundo.")

class CSVWriterFilter:
    def __init__(self, output_file_path):
        self.output_file_path = output_file_path

    def process(self, pipe):
        data = pipe.get_data()
        if not data:
            logger.warning(f"Nenhum dado para salvar no arquivo {self.output_file_path}.")
            return

        logger.info(f"Salvando dados filtrados no arquivo CSV: {self.output_file_path}")
        start_time = time.time()
        with open(self.output_file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        end_time = time.time()
        duration = end_time - start_time
        throughput = len(data) / duration if duration > 0 else float('inf')
        logger.info(f"Dados filtrados foram salvos em {self.output_file_path}. Tempo de salvamento: {duration:.4f} segundos. Throughput: {throughput:.2f} registros/segundo.")

def process_csv(file_path, output_file_path):
    start_time = time.time()
    
    pipe = Pipe()
    reader = CSVReaderFilter(file_path)
    alta_filter = AltaFilter()
    age_filter = AgeFilter(min_age=40)
    writer = CSVWriterFilter(output_file_path)
    
    reader.process(pipe)
    alta_filter.process(pipe)
    age_filter.process(pipe)
    writer.process(pipe)
    
    end_time = time.time()
    total_throughput = len(pipe.get_data()) / (end_time - start_time) if (end_time - start_time) > 0 else float('inf')
    logger.info(f"Tempo total de execução do pipeline para {file_path}: {end_time - start_time:.4f} segundos. Throughput total: {total_throughput:.2f} registros/segundo.")

def pipe_and_filter_example():
    # Processa o primeiro arquivo CSV
    process_csv('dados_hospital.csv', 'dados_hospital_resultado.csv')

    # Processa o segundo arquivo CSV
    process_csv('dados_hospital_100.csv', 'dados_hospital_resultado1.csv')

if __name__ == "__main__":
    pipe_and_filter_example()
