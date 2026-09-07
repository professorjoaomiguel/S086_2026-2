# Arduino IDE - Guia Técnico S086

## 1. Visão Geral (O Básico)
**Para que serve:** IDE (ambiente de desenvolvimento) oficial usada para escrever, compilar e enviar (upload) código C/C++ para as placas físicas do curso.
**Placas aplicáveis:** [X] Arduino UNO R3 | [X] ESP32-S3-UNO | [X] Shield 9-em-1 | [X] Todas

## 2. Fluxo de Dados (I/O)
- **Entrada (Input):** Código-fonte C/C++ (sketch `.ino`) escrito pelo aluno.
- **Saída (Output):** Firmware compilado, enviado via USB para a placa; feedback de compilação/upload no próprio IDE.

## 3. Instalação e Configuração

### 🪟 Windows (caminho padrão — "next, next, next")
1. Baixe o instalador oficial em https://www.arduino.cc/en/software → botão "Windows". Não é necessário o ZIP portable nem a versão beta.
2. Rode o instalador com as opções padrão e aceite a instalação de drivers USB quando solicitado — é isso que permite ao Windows reconhecer as placas.
3. Na primeira abertura, o Windows/antivírus pode pedir confirmação de execução — permita.

> Alunos que já têm o Arduino IDE instalado: confiram se a versão é 2.x (Help > About). Este guia não cobre a série 1.8.x.

### 🐧 Linux (opcional, fora do laboratório SENAI)
1. Baixe o AppImage em https://www.arduino.cc/en/software, dê permissão de execução (`chmod +x`) e rode.
2. Adicione seu usuário ao grupo `dialout` para acessar a porta serial sem `sudo` (`sudo usermod -aG dialout $USER`, depois faça logout/login).

### Configuração inicial (fazer antes da primeira aula prática)
1. **Local dos sketches:** File > Preferences > Sketchbook location.
   - Padrão do Windows: `Documents\Arduino`.
   - ⚠️ **Atenção OneDrive:** se o computador sincroniza a pasta Documentos com o OneDrive (comum em notebook institucional/corporativo), esse caminho na verdade é `OneDrive\Documents\Arduino` — a sincronização em nuvem pode travar arquivos durante a compilação, causando erros aleatórios de upload. Recomendação: aponte o Sketchbook location para uma pasta fora do OneDrive, ex.: `C:\Arduino\`.
2. **Core da placa ESP32 (necessário para a ESP32-S3-UNO):** Tools > Board > Boards Manager, procure e instale "esp32 by Espressif Systems". Faça isso com internet boa e fora do horário de aula — o download é de ~1-2 GB na primeira vez. O Arduino UNO R3 não precisa de core adicional (já vem com o IDE).
3. **Driver CH340 (bridge USB-serial da ESP32-S3-UNO):** se a placa não aparecer em Tools > Port ao conectar via USB, o driver CH340 pode não ter sido instalado automaticamente — baixe em http://www.wch-ic.com/downloads/CH341SER_EXE.html e instale manualmente.
4. **Bibliotecas do curso**, se houver lista definida: Sketch > Include Library > Manage Libraries.

### Organização dos sketches
- Cada sketch é uma pasta com um arquivo `.ino` de mesmo nome — não crie estrutura diferente; o próprio IDE já faz isso corretamente ao clicar em "New Sketch".
- Nomeie sem acento, espaço ou caractere especial: use `sensor_temperatura`, não `Sensor de Temperatura`. Nomes com acento podem quebrar a compilação.
- Sugestão: uma subpasta por atividade/aula dentro do Sketchbook (`aula03_blink`, `projeto_final`, etc.) — facilita achar e entregar depois.

### Se o computador é compartilhado/do laboratório
- Confirme o Sketchbook location (passo 1 acima) toda vez que sentar numa máquina diferente — pode estar apontando para a pasta de outro aluno/turma.
- Salve seu trabalho também num pendrive ou no seu próprio OneDrive/Google Drive ao final da aula — nada garante que a pasta local sobreviva até a próxima aula.

### Checklist rápido antes de começar a programar
- [ ] Arduino IDE 2.x instalado
- [ ] Sketchbook location definido e fora de pasta sincronizada com nuvem
- [ ] Core ESP32 instalado (Boards Manager) — necessário só para a ESP32-S3-UNO
- [ ] Driver CH340 instalado (se a ESP32-S3-UNO não aparecer em Tools > Port)
- [ ] Bibliotecas do curso instaladas (se houver)
- [ ] Placa reconhecida em Tools > Port quando conectada via USB

## 4. Integração (Ecossistema S086)
- **Conecta com:** [Wokwi](https://wokwi.com) — permite simular circuito e código antes de ir para a placa física (guia próprio a ser adicionado a este diretório).
- **Depende de:** nenhum pré-requisito de software; depende de acesso à internet para instalar o core ESP32 na primeira configuração.

## 5. Referências e Repositórios
- **Documentação Oficial:** https://docs.arduino.cc/software/ide-v2/
- **Core ESP32 (Espressif):** https://github.com/espressif/arduino-esp32
- **Driver CH340:** http://www.wch-ic.com/downloads/CH341SER_EXE.html
- **Referência de hardware das placas:** [`lab_dev_boards`](https://github.com/professorjoaomiguel/lab_dev_boards)

## 6. Solução de Problemas (Troubleshooting)
- **Placa não aparece em Tools > Port:** verifique o driver CH340 (ESP32-S3-UNO) ou troque o cabo USB — alguns cabos são só de carga, sem linhas de dados.
- **Erro de upload aleatório/intermitente:** verifique se o Sketchbook location está fora de uma pasta sincronizada com OneDrive (ver seção 3).
- **ESP32-S3-UNO não aparece na lista de placas em Tools > Board:** confirme que o core "esp32 by Espressif Systems" foi instalado via Boards Manager.
- **Compilação falha sem motivo aparente:** verifique se o nome da pasta/sketch tem acento, espaço ou caractere especial.

## 7. Fontes de Consulta (AI & Web)
- Rascunho inicial elaborado com apoio de assistente de IA (Claude Code), revisado e adaptado às placas específicas do S086 (ESP32-S3-UNO, CH340, Arduino UNO R3).
- Documentação oficial listada na seção 5.

---
*Documento em constante atualização. Versão: 2026/2*
