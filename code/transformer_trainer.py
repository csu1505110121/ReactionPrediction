from onmt.train_single import main as single_main
from onmt.new_opts import Opts

opt = Opts(
        max_grad_norm=0,
        param_init=0,
        param_init_glorot=True,
        heads=4,
        tgt_word_vec_size=256,
        src_word_vec_size=256,
        transformer_ff=1024,
        position_encoding=True,
        max_generator_batches=2,
        train_steps=1000000,
        dropout=0.1,
        data="data/USP",
        save_model="models/transformer_model",
        batch_size=4096,
        gpu_ranks=[0],
        valid_steps=1000,
        valid_batch_size=8,
        optim="adam",
        learning_rate=1.,
        save_checkpoint_steps=1000,
        encoder_type="transformer",
        decoder_type="transformer",
        enc_layers=4,
        dec_layers=4,
        enc_rnn_size=256,
        dec_rnn_size=256,
        normalization="tokens",
        batch_type="tokens",
        adam_beta2=0.98,
        adam_beta1=0.9,
        accum_count=4,
        decay_method="noam",
        warmup_steps=8000,
        rnn_size=256,
          )
single_main(opt, -1)
