# information_system_design_project
Project for the course information system design from the university.

The main aim is to learn how to connect RESTful API and gRPC using Python. In future may be added using of Docker.

## How to start
Follow next steps:

1. Cloning of this repository
```bash
git clone https://github.com/MiniDan21/information_system_design_project
```
and
```bash
cd information_system_design_project
```

2. Preparing dot-env file
```bash
cp .env.example .env
```

3. Setup virtual environment
```bash
./tools/setup.sh
```

4. Starting demo
```bash
./tools/start.sh
```

5. Testing
```bash
./tools/tests
```

6. If you change code, then use linting
```bash
./tools/linting.sh
```