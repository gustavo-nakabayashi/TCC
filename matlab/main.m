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
        file_csv = load(fullFileName);

        open_price_data = file_csv(:,2:2);
        high_price_data = file_csv(:,3:3);
        low_price_data  = file_csv(:,4:4);
        
        % Dados baixa
        [epm, acerto_percentual, ys] = previsor(low_price_data, open_price_data);
        epm_row = [epm_row;epm];
        acerto_percentual_row = [acerto_percentual_row;acerto_percentual];
        name_row = [name_row; fileName(1)];
        write_data = [file_csv((length(high_price_data) - length(ys) + 1):end,1:1), ys'];
        
        % Dados baixa
        [epm, acerto_percentual, ys] = previsor(high_price_data, open_price_data);
        epm_row = [epm_row;epm];
        acerto_percentual_row = [acerto_percentual_row;acerto_percentual];
        name_row = [name_row; fileName(1)];
        
        write_data = [write_data, ys'];
        
        % Add real volume
        write_data = [write_data, file_csv((length(high_price_data) - length(ys) + 1):end,8:8)];

        baseFileName = erase(baseFileName, "_without");
        writematrix(write_data,"..\previsions\" + baseFileName ,'Delimiter',',')

    end
end

table(name_row,epm_row,acerto_percentual_row)