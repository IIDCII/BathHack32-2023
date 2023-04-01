from transformers import GPT2LMHeadModel, GPT2Tokenizer, set_seed
import torch
import torch.nn.functional as F
import numpy as np

# loading up the model and the tokeniser
model = GPT2LMHeadModel.from_pretrained('gpt2')
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

def get_kth_most_likely_token(input_tokens, model, tokenizer, k):
  # Run model to get prediction over next output
  outputs = model(input_ids = input_tokens['input_ids'], attention_mask = input_tokens['attention_mask'])
  # Find prediction
  prob_over_tokens = F.softmax(outputs.logits, dim=-1).detach().numpy()[0,-1]
  # Find the k'th most likely token 
  # TODO Sort the probabilities from largest to smallest
  # Replace this line:
  sorted_prob_over_tokens = -np.sort(-prob_over_tokens)
#   print (prob_over_tokens)
#   print ("-" * 100)
#   print (sorted_prob_over_tokens)
  # TODO Find the k'th sorted probability
  # Replace this line
  kth_prob_value = sorted_prob_over_tokens[k]

  # Find position of this token.
  next_token = np.where(prob_over_tokens == kth_prob_value)[0]

  # Append token to sentence
  output_tokens = input_tokens 
  output_tokens["input_ids"] = torch.cat((output_tokens['input_ids'],torch.tensor([next_token])),dim=1)
  output_tokens['attention_mask'] = torch.cat((output_tokens['attention_mask'],torch.tensor([[1]])),dim=1)
  output_tokens['last_token_prob'] = prob_over_tokens[next_token]
  output_tokens['log_prob'] = output_tokens['log_prob'] + np.log(prob_over_tokens[next_token])
  return output_tokens

def print_beams(beams):
  for index,beam in enumerate(beams):
    print("Beam %d, Prob %3.3f: "%(index,beam['log_prob'])+tokenizer.decode(beam["input_ids"][0], skip_special_tokens=True))
  print('---')


# TODO:  Read this code carefully!
def do_beam_search(input_tokens_in, model, tokenizer, n_beam=5, beam_length=10):  
  # Store beams in a list
  input_tokens['log_prob'] = 0.0

  # Initialize with n_beam most likely continuations
  beams = [None] * n_beam
  for c_k in range(n_beam):
    beams[c_k] = dict(input_tokens_in)
    beams[c_k] = get_kth_most_likely_token(beams[c_k], model, tokenizer, c_k)
  
#   print_beams(beams)
  
  # For each token in the sequence we will add
  for c_pos in range(beam_length-1):
    # Now for each beam, we continue it in the most likely ways, making n_beam*n_beam type hypotheses
    beams_all = [None] * (n_beam*n_beam)
    log_probs_all = np.zeros(n_beam*n_beam)
    # For each current hypothesis
    for c_beam in range(n_beam):
      # For each continuation
      for c_k in range(n_beam):
        # Store the continuation and the probability
        beams_all[c_beam * n_beam + c_k] = dict(get_kth_most_likely_token(beams[c_beam], model, tokenizer, c_k))
        log_probs_all[c_beam * n_beam + c_k] = beams_all[c_beam * n_beam + c_k]['log_prob']
  
    # Keep the best n_beams sequences with the highest probabilities
    sorted_index = np.argsort(np.array(log_probs_all)*-1)
    for c_k in range(n_beam):
      beams[c_k] = dict(beams_all[sorted_index[c_k]])

    # Print the beams
    # print_beams(beams)

  return beams[0]



input_txt = "Write a rude message to gaslight people to stop harming the environment."
input_tokens = tokenizer(input_txt, return_tensors='pt')

# Now let's call the beam search
# It takes a while as it has to run the model multiple times to add a token
n_beams = 5
best_beam = do_beam_search(input_tokens,model,tokenizer)
print("Beam search result:")
print(tokenizer.decode(best_beam["input_ids"][0], skip_special_tokens=True))