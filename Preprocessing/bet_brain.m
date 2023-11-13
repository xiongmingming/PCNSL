clear ;
clc;
close all;
path_save = '/home/xiong/bet/';
path_LGG='/home/xiong/BET/question/';

path_LGG_dir = fullfile(path_LGG);
LGG_dir = dir(fullfile(path_LGG_dir,'*'));
LGG_dir_name = {LGG_dir(3:end).name}';
for i = 1:length(LGG_dir_name)
    save_path1 = strcat(path_save,LGG_dir_name{i},'/');
    if ~exist(save_path1,'file')==1
        mkdir(save_path1);
    end
    LGG_name = strcat(path_LGG,LGG_dir_name{i},'/');
    path_LGG_dir_2 = fullfile(LGG_name);
    LGG_dir_2 = dir(fullfile(path_LGG_dir_2,'*'));
    LGG_dir_name2 = {LGG_dir_2(3:end).name}';
    A = sprintf(LGG_dir_name{i});
    disp(A);
    for j = 1:length(LGG_dir_name2)
        name = LGG_dir_name2{j};
        path_nii = strcat(LGG_name,LGG_dir_name2{j});
        save_nii = strcat(save_path1,LGG_dir_name2{j});
        cmdstr = strcat('/home/xiong/fsl/bin/bet',32,path_nii,32,save_nii,32,'-f 0.5'); 
        disp(cmdstr);
        system(cmdstr);
    end
end