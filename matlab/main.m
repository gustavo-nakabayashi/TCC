addpath('..\data\')
addpath('..\matlab\')
filePattern = fullfile("..\data\", '*.csv');
dir(filePattern)
theFiles = dir(filePattern);
epm_row = [];
acerto_percentual_row = [];
name_row = [];

for k = 1 : length(theFiles)
    baseFileName = theFiles(k).name;
    fullFileName = fullfile(theFiles(k).folder, baseFileName);
    fileName = split(string(baseFileName), ".");
    if contains(baseFileName,"without.csv")
        fprintf(1, 'Now reading %s\n', fullFileName);
        teste = load(fullFileName);
        
        
        open_price_data = teste(:,2:2);
        high_price_data = teste(:,3:3);
        low_price_data  = teste(:,4:4);
        

        [epm, acerto_percentual, ys] = previsor(low_price_data, open_price_data);
        epm_row = [epm_row;epm];
        acerto_percentual_row = [acerto_percentual_row;acerto_percentual];
        name_row = [name_row; fileName(1)];
        write_data = [teste((length(high_price_data) - length(ys) + 1):end,1:1), ys'];


        [epm, acerto_percentual, ys] = previsor(high_price_data, open_price_data);
        epm_row = [epm_row;epm];
        acerto_percentual_row = [acerto_percentual_row;acerto_percentual];
        name_row = [name_row; fileName(1)];

        write_data = [write_data, ys'];

        baseFileName = erase(baseFileName, "_without");
        writematrix(write_data,"..\previsions\" + baseFileName ,'Delimiter',',')

    end
end

table(name_row,epm_row,acerto_percentual_row)