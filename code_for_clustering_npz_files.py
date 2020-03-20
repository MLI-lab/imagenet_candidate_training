out_npz = out_dir / 'data' / 'candididate'
out_npz.mkdir(parents=True, exist_ok=True) 

im_arr = []
lbl_arr = []
save_idx = 1
save_lim = 2000
for cur_idx in tqdm(rand_idx):
    
    if cur_idx < npz_size_list[0] - 1:
        cur_npz_file = npz_list[0]
        cur_npz_idx = cur_idx
    
    elif cur_idx > sum(npz_size_list[:-1]) - 1:
        cur_npz_file = npz_list[-1]
        cur_npz_idx = cur_idx - sum(npz_size_list[:-1])
        
    else:
    
        for i in range(1, len(npz_size_list)):
            size_1 = sum(npz_size_list[:i-1]) - 1
            size_2 = size_1 + npz_size_list[i]
            
            if (cur_idx > size_1) and (cur_idx < size_2):
                cur_npz_file = npz_list[i]
                cur_npz_idx = cur_idx - (size_1 + 1)
                break
                
    im_arr.append(np.load(cur_npz_file)['X_train'][cur_npz_idx])
    lbl_arr.append(chosen_dict[str(cur_npz_file).split('downloads/')[-1].split('/')[0]])
    
    if len(im_arr) >= save_lim:
        out_npz_file = out_npz / ('candidate_batch_' + str(save_idx) + '.npz')
        X_train = np.array(im_arr)
        y_train = np.array(lbl_arr)
        
        np.savez(out_npz_file, X_train=X_train, y_train=y_train)
        save_idx += 1
        
        print('[PROG]: saved npz file'.format(out_npz_file))
        
        im_arr = []
        lbl_arr = []
