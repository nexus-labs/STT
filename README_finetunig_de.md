# Fine-tuning from pre-trained model in German

## Installation
Install this repogitory and dependencies under Python3 environment
```
clone https://github.com/nexus-labs/DeepSpeech -b finetuning_0.6.0
cd DeepSpeech
pip3 install -r requirements.txt
```

## Fine-tuning
### Download pre-trained model
Download the deepspeech model and LM form the link below.
https://drive.google.com/drive/folders/1BKblYaSLnwwkvVOQTQ5roOeN0SuQm8qr

### Prepare dataset
Put audio files (default=16kHz/16bit) to your own paths and make manifest csv files for train, development, test.

Manifest file example:
```
wav_filename,wav_filesize,transcript
data/callhome/train/5298/5298_A_0000_16k.wav,22334,dreizehn uh
data/callhome/train/5298/5298_A_0002_16k.wav,42974,mhm wahnsinn
data/callhome/train/5298/5298_B_0003_16k.wav,32414,ja ist wahnsinn ne
```

### Training
For 16kHz audio:
```
python3 DeepSpeech.py \
	--checkpoint_dir $PRETRAIND_MODEL \
	--audio_sample_rate 16000 \
	--alphabet_config_path  $PRETRAIND_MODEL/alphabet.txt \
	--train_files data/callhome/callhome_german_train_16k.csv \
	--dev_files data/callhome/callhome_german_dev_16k.csv \
	--train_batch_size 48 \
	--dev_batch_size 48 \
	--learning_rate 0.0001 \
	--dropout_rate 0.3 \
	--early_stop True \
	--best_checkpoint_dir deepspeech-de-finetuning-16k-checkpoint \
	--export_dir deepspeech-de-finetuning-16k \
	--summary_dir summry_deepspeech-de-finetuning-16k
```
For 8kHz audio:
```
python3 DeepSpeech.py \
	--checkpoint_dir $PRETRAIND_MODEL \
	--audio_sample_rate 8000 \
	--drop_source_layers 1 \
	--alphabet_config_path  $PRETRAIND_MODEL/alphabet.txt \
	--train_files data/callhome/callhome_german_train_8k.csv \
	--dev_files data/callhome/callhome_german_dev_8k.csv \
	--train_batch_size 48 \
	--dev_batch_size 48 \
	--learning_rate 0.0001 \
	--dropout_rate 0.3 \
	--early_stop True \
	--best_checkpoint_dir deepspeech-de-finetuning-8k-checkpoint \
	--export_dir deepspeech-de-finetuning-8k \
	--summary_dir summry_deepspeech-de-finetuning-8k
```

### Test
For 16kHz audio:
```
python3  DeepSpeech.py \
	--lm $PRETRAIND_MODEL/lm.binary \
	--trie $PRETRAIND_MODEL/trie \
	--checkpoint_dir deepspeech-de-finetuning-16k-checkpoint \
	--audio_sample_rate 16000 \
	--alphabet_config_path $PRETRAIND_MODEL/alphabet.txt \
	--load 'best' \
	--test_files data/callhome/callhome_german_test_16k.csv  \
	--test_batch_size 48 \
	--test_output_file deepspeech-de-finetuning-16k.json
```
For 8kHz audio:
```
python3  DeepSpeech.py \
	--lm $PRETRAIND_MODEL/lm.binary \
	--trie $PRETRAIND_MODEL/trie \
	--checkpoint_dir deepspeech-de-finetuning-8k-checkpoint \
	--audio_sample_rate 8000 \
	--alphabet_config_path $PRETRAIND_MODEL/alphabet.txt \
	--load 'best' \
	--test_files data/callhome/callhome_german_test_8k.csv  \
	--test_batch_size 48 \
	--test_output_file deepspeech-de-finetuning-8k.json
```